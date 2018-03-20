# -*- coding: utf-8 -*-
from estacion.models import Estacion
from variable.models import Variable
from medicion.models import Medicion
from registro.models import LogMedicion
from datetime import datetime,timedelta,date
from django.db import connection
from django.contrib.auth.models import User

import plotly.offline as opy
import plotly.graph_objs as go

def filtrar(form):
    estacion=form.cleaned_data['estacion']
    variable=form.cleaned_data['variable']
    inicio=form.cleaned_data['inicio']
    fin=form.cleaned_data['fin']
    year_ini=inicio.strftime('%Y')
    year_fin=fin.strftime('%Y')
    var_cod=variable.var_codigo
    if year_ini==year_fin:
        tabla=var_cod+'.m'+year_ini
        sql='SELECT * FROM '+tabla+ ' WHERE '
        sql+='est_id_id='+str(estacion.est_id)+ ' and '
        sql+='med_fecha>=\''+str(inicio)+'\' and '
        sql+='med_fecha<=\''+str(fin)+'\' and med_estado is not False '
        sql+='order by med_fecha'
        print sql
        consulta=list(Medicion.objects.raw(sql))
    else:
        range_year=range(int(year_ini),int(year_fin)+1)
        consulta=[]
        for year in range_year:
            tabla=var_cod+'.m'+str(year)
            if str(year)==year_ini:
                sql='SELECT * FROM '+tabla+ ' WHERE '
                sql+='est_id_id='+str(estacion.est_id)+ ' and '
                sql+='med_fecha>=\''+str(inicio)+'\' med_estado is not False '
                sql+='order by med_fecha'
            elif str(year)==year_fin:
                sql='SELECT * FROM '+tabla+ ' WHERE '
                sql+='est_id_id='+str(estacion.est_id)+ ' and '
                sql+='med_fecha<=\''+str(fin)+'\' med_estado is not False '
                sql+='order by med_fecha'

            else:
                sql='SELECT * FROM '+tabla+ ' WHERE '
                sql+='est_id_id='+str(estacion.est_id)+' med_estado is not False '
                sql+='order by med_fecha'
            print sql
            consulta.extend(list(Medicion.objects.raw(sql)))

    #parametros para la resta consecutiva
    i=0
    ans=0
    datos=[]
    #parametros para la variabilidad
    valor_acumulado=0
    xi_acumulado=0
    hora0=datetime.strptime("00:00:00","%H:%M:%S")
    dat_var=[] #almacena las mediciones de una hora
    variabilidad=0
    for item in consulta:
        obj_analisis=Analisis()
        valor=item.med_valor
        valor_error=False
        resta=0
        resta_error=False
        var_error=False
        if valor<variable.var_minimo or valor>variable.var_maximo:
            valor_error=True
        if variable.var_sos is None and variable.var_err is None:
            resta=""
            resta_error="no aplica"
        else:
            #calculo de la resta consecutiva
            if i==0:
                resta=0
                ans=valor
                hora0=item.med_fecha
            else:
                resta=valor-ans
                ans=valor
            i+=1
            if resta<variable.var_sos:
                resta_error="normal"
            elif resta>=variable.var_sos and resta<variable.var_err:
                resta_error="sospechoso"
            elif resta>=variable.var_err:
                resta_error="error"
            resta=abs(resta)

        #variabilidad
        if variable.var_min is None:
            variabilidad=""
            var_error=None
        else:
            dif_minutos=int(item.med_fecha.minute)-int(hora0.minute)
            dif_hora=int(item.med_fecha.hour)-int(hora0.hour)
            valor_acumulado+=valor
            dat_var.append(item.med_valor)
            if (dif_minutos==58 and len(dat_var)==30) or (dif_minutos==59 and len(dat_var)==60) and dif_hora<1:
                promedio=sum(dat_var)/len(dat_var)
                for val in dat_var:
                    xi_acumulado+=(val-promedio)**2
                variabilidad=float(xi_acumulado/len(dat_var)) ** 0.5
                dat_var=[]
                valor_acumulado=0
                xi_acumulado=0
            elif dif_hora>=1:
                hora0=item.med_fecha
                variabilidad=0
            if variabilidad<variable.var_min:
                var_error=True

        #asignar al objeto analisis
        obj_analisis.med_id=item.med_id
        obj_analisis.var_id=item.var_id.var_id
        obj_analisis.fecha=item.med_fecha.date
        obj_analisis.hora=item.med_fecha.time
        obj_analisis.valor=item.med_valor
        obj_analisis.valor_error=valor_error
        obj_analisis.resta=resta
        obj_analisis.resta_error=resta_error
        obj_analisis.variabilidad=variabilidad
        obj_analisis.var_error=var_error
        datos.append(obj_analisis)
    return datos
def consultar_objeto(kwargs):
    med_id=kwargs.get('pk')
    med_fecha=kwargs.get('fecha')
    var_id=kwargs.get('var_id')
    fecha_split=med_fecha.split("-")
    variable=Variable.objects.get(var_id=var_id)
    year=fecha_split[0]
    var_cod=variable.var_codigo
    tabla=var_cod+'.m'+year
    sql='SELECT * FROM '+tabla+ ' WHERE '
    sql+='med_id='+str(med_id)
    consulta=list(Medicion.objects.raw(sql))
    print sql
    return consulta[0]
def modificar_medicion(kwargs,data):
    med_id=kwargs.get('pk')
    med_fecha=kwargs.get('fecha')
    var_id=kwargs.get('var_id')
    fecha_split=med_fecha.split("-")
    variable=Variable.objects.get(var_id=var_id)
    year=fecha_split[0]
    var_cod=variable.var_codigo
    tabla=var_cod+'.m'+year
    if str(data.get('med_maximo'))=='':
        med_maximo='Null'
    else:
        med_maximo=str(data.get('med_maximo'))
    if str(data.get('med_minimo'))=='':
        med_minimo='Null'
    else:
        med_minimo=str(data.get('med_maximo'))
    sql="UPDATE "+tabla+" SET med_valor = "+str(data.get('med_valor'))
    sql+=", med_maximo="+med_maximo+", med_minimo="
    sql+=med_minimo+"  WHERE med_id = "+str(med_id)
    with connection.cursor() as cursor:
        cursor.execute(sql)
def eliminar_medicion(kwargs,data):
    med_id=kwargs.get('pk')
    med_fecha=kwargs.get('fecha')
    var_id=kwargs.get('var_id')
    fecha_split=med_fecha.split("-")
    variable=Variable.objects.get(var_id=var_id)
    year=fecha_split[0]
    var_cod=variable.var_codigo
    tabla=var_cod+'.m'+year
    sql="UPDATE "+tabla+" SET med_estado = false "
    sql+="WHERE med_id = "+str(med_id)
    print sql
    with connection.cursor() as cursor:
        cursor.execute(sql)
#funcion para registrar los cambios en la tabla medicion
def guardar_log(accion,medicion,user):
    logmedicion=LogMedicion()
    logmedicion.medicion=medicion.med_id
    logmedicion.variable=medicion.var_id
    logmedicion.estacion=medicion.est_id
    logmedicion.marca=medicion.mar_id
    logmedicion.med_fecha=medicion.med_fecha
    logmedicion.med_valor=medicion.med_valor
    logmedicion.med_maximo=medicion.med_maximo
    logmedicion.med_minimo=medicion.med_minimo
    logmedicion.usuario=user
    logmedicion.log_accion=accion
    if accion=="Modificar":
        logmedicion.log_mensaje="Valores Modificados"
    else:
        logmedicion.log_mensaje="Valores Eliminados"
    logmedicion.save()

def consultar(form):
    estacion=form.cleaned_data['estacion']
    variable=form.cleaned_data['variable']
    inicio=form.cleaned_data['inicio']
    fin=form.cleaned_data['fin']
    year_ini=inicio.strftime('%Y')
    year_fin=fin.strftime('%Y')
    var_cod=variable.var_codigo
    if year_ini==year_fin:
        tabla=var_cod+'.m'+year_ini
        sql='SELECT * FROM '+tabla+ ' WHERE '
        sql+='est_id_id='+str(estacion.est_id)+ ' and '
        sql+='med_fecha>=\''+str(inicio)+'\' and '
        sql+='med_fecha<=\''+str(fin)+'\' and med_estado is not False '
        sql+='order by med_fecha'
        print sql
        consulta=list(Medicion.objects.raw(sql))
    else:
        range_year=range(int(year_ini),int(year_fin)+1)
        consulta=[]
        for year in range_year:
            tabla=var_cod+'.m'+str(year)
            if str(year)==year_ini:
                sql='SELECT * FROM '+tabla+ ' WHERE '
                sql+='est_id_id='+str(estacion.est_id)+ ' and '
                sql+='med_fecha>=\''+str(inicio)+'\' med_estado is not False '
                sql+='order by med_fecha'
            elif str(year)==year_fin:
                sql='SELECT * FROM '+tabla+ ' WHERE '
                sql+='est_id_id='+str(estacion.est_id)+ ' and '
                sql+='med_fecha<=\''+str(fin)+'\' med_estado is not False '
                sql+='order by med_fecha'

            else:
                sql='SELECT * FROM '+tabla+ ' WHERE '
                sql+='est_id_id='+str(estacion.est_id)+' med_estado is not False '
                sql+='order by med_fecha'
            print sql
            consulta.extend(list(Medicion.objects.raw(sql)))

    return consulta
def eliminar(form):
    est_id=str(form.cleaned_data['estacion'])
    var_id=str(form.cleaned_data['variable'])
    fec_ini=str(form.cleaned_data['fec_ini'])+str(" ")+str(form.cleaned_data['hor_ini'])
    fec_fin=str(form.cleaned_data['fec_fin'])+str(" ")+str(form.cleaned_data['hor_fin'])
    print (str(form.cleaned_data['fec_ini'])+str(form.cleaned_data['hor_ini']))
    with connection.cursor() as cursor:
        cursor.execute("UPDATE medicion_medicion SET med_estado = false \
        WHERE est_id_id=%s\
        and var_id_id=%s and med_fecha>=%s \
        and med_fecha<=%s",
        [est_id,var_id,fec_ini,fec_fin] )
    return "Proceso Realizado"
def grafico(consulta,variable,estacion):
    valor=[]
    maximo=[]
    minimo=[]
    frecuencia=[]
    for fila in consulta:
        valor.append(fila.med_valor)
        maximo.append(fila.med_maximo)
        minimo.append(fila.med_minimo)
        frecuencia.append(fila.med_fecha)
    if variable.var_id==1:
        trace = go.Bar(
            x=frecuencia,
            y=valor,
            name='Precipitacion (mm)'
        )
        data = go.Data([trace])
    elif variable.var_id in [6,8,9,10,11]:
        trace0 = go.Scatter(
            x = frecuencia,
            y = maximo,
            name = 'Max',
            mode = 'lines',
            line = dict(
                color = ('rgb(205, 12, 24)'),
                )
        )
        trace1 = go.Scatter(
            x = frecuencia,
            y = minimo,
            name = 'Min',
            mode = 'lines',
            line = dict(
                color = ('rgb(50, 205, 50)'),
                )
        )
        trace2 = go.Scatter(
            x = frecuencia,
            y = valor,
            name = 'Media',
            mode = 'lines',
            line = dict(
                color = ('rgb(22, 96, 167)'),
                )
        )
        data = go.Data([trace0,trace1,trace2])
    else:
        trace = go.Scatter(
            x = frecuencia,
            y = valor,
            name = 'Valor',
            mode = 'lines',
            line = dict(
                color = ('rgb(205, 12, 24)'),
                )
        )
        data = go.Data([trace])
    layout = go.Layout(
        title = estacion.est_codigo+" "+estacion.est_nombre,
        yaxis = dict(title = variable.var_nombre),
        )
    figure = go.Figure(data=data, layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')
    return div
def titulo_unidad(variable):
    uni=list(Unidad.objects.filter(uni_id=variable.uni_id.uni_id).values())
    return uni[0].get('uni_sigla')

class Analisis(object):
    med_id=0
    var_id=0
    fecha=""
    hora=""
    valor=0
    valor_error=False
    resta=0
    resta_error="Normal"
    variabilidad=0
    var_error=False
