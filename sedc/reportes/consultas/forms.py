# -*- coding: utf-8 -*-
from django import forms
from estacion.models import Estacion
from variable.models import Variable, Unidad
from medicion.models import Medicion
from django.db.models import Max, Min, Avg, Count,Sum
from django.db.models.functions import (
    ExtractYear,ExtractMonth,ExtractDay,ExtractHour)
import plotly.offline as opy
import plotly.graph_objs as go
import datetime, calendar


from django.db import connection
#cursor = connection.cursor()

class MedicionSearchForm(forms.Form):
    def lista_year():
        lista=()
        periodos=Medicion.objects.annotate(year=ExtractYear('med_fecha')).values('year').distinct('year')
        for item in periodos:
            i=((item.get('year'),item.get('year')),)
            lista=lista+i
        return lista
    FRECUENCIA=(
        ('0','Minima'),
        ('1','5 Minutos'),
        #('2','Horario'),
        #('3','Diario'),
        #('4','Mensual'),
    )
    estacion=forms.ModelChoiceField(
        queryset=Estacion.objects.order_by('est_id').all())
    variable=forms.ModelChoiceField(
        queryset=Variable.objects.order_by('var_id').all())

    inicio=forms.DateField(input_formats=['%d/%m/%Y'],label="Fecha de Inicio(dd/mm/yyyy)")
    fin=forms.DateField(input_formats=['%d/%m/%Y'],label="Fecha de Fin(dd/mm/yyyy)")
    frecuencia=forms.ChoiceField(choices=FRECUENCIA)
    #saber si hay datos
    def exists(self,form):
        #print self.estacion
        estacion=form.cleaned_data['estacion']
        variable=form.cleaned_data['variable']
        fecha_inicio=form.cleaned_data['inicio']
        fecha_fin=form.cleaned_data['fin']
        frecuencia=form.cleaned_data['frecuencia']
        #filtrar los datos por estacion, variable y rango de fechas
        consulta=(Medicion.objects.filter(est_id=estacion)
        .filter(var_id=variable)
        .filter(med_fecha__range=[fecha_inicio,fecha_fin]).exists())
        return consulta


    #consulta para agrupar los datos por hora, diario y mes
    def filtrar(self,form):
        #filtrar los datos por estacion, variable y rango de fechas
        estacion=form.cleaned_data['estacion']
        variable=form.cleaned_data['variable']
        fecha_inicio=form.cleaned_data['inicio']
        fecha_fin=form.cleaned_data['fin']
        frecuencia=form.cleaned_data['frecuencia']
        #filtrar los datos por estacion, variable y rango de fechas
        consulta=(Medicion.objects.filter(est_id=estacion)
        .filter(var_id=variable).filter(med_fecha__range=[fecha_inicio,fecha_fin]))

        #frecuencia instantanea
        if(frecuencia==str(0)):
            year_ini=fecha_inicio.strftime('%Y')
            year_fin=fecha_fin.strftime('%Y')
            var_cod=variable.var_codigo
            if year_ini==year_fin:
                tabla=var_cod+'.m'+year_ini
                sql='SELECT * FROM '+tabla+ ' WHERE '
                sql+='est_id_id='+str(estacion.est_id)+ ' and '
                sql+='med_fecha>=\''+str(fecha_inicio)+'\' and '
                sql+='med_fecha<=\''+str(fecha_fin)+'\''
                print sql
                datos=list(Medicion.objects.raw(sql))
            else:
                range_year=range(int(year_ini),int(year_fin)+1)
                datos=[]
                for year in range_year:
                    tabla=var_cod+'.m'+str(year)
                    if str(year)==year_ini:
                        sql='SELECT * FROM '+tabla+ ' WHERE '
                        sql+='est_id_id='+str(estacion.est_id)+ ' and '
                        sql+='med_fecha>=\''+str(fecha_inicio)+'\''
                    elif str(year)==year_fin:
                        sql='DELETE FROM '+tabla+ ' WHERE '
                        sql+='est_id_id='+str(est_id)+ ' and '
                        sql+='med_fecha<=\''+str(fecha_fin)+'\''

                    else:
                        sql='DELETE FROM '+tabla+ ' WHERE '
                        sql+='est_id_id='+str(estacion.est_id)
                    print sql
                    datos.append(list(Medicion.objects.raw(sql)))
        #cada 5 min
        elif(frecuencia==str(1)):
            year_ini=fecha_inicio.strftime('%Y')
            year_fin=fecha_fin.strftime('%Y')
            var_cod=variable.var_codigo
            cursor = connection.cursor()
            if year_ini==year_fin:
                tabla=var_cod+'.m'+year_ini
                if variable.var_id==1:
                    sql='SELECT sum(med_valor) as valor, '
                    sql+='to_timestamp(floor((extract(\'epoch\' '
                    sql+='from med_fecha) / 300 )) * 300)'
                    sql+='AT TIME ZONE \'UTC5\' as interval_alias '
                    sql+='FROM '+tabla+ ' WHERE '
                    sql+='est_id_id='+str(estacion.est_id)+ ' and '
                    sql+='med_fecha>=\''+str(fecha_inicio)+'\' and '
                    sql+='med_fecha<=\''+str(fecha_fin)+'\''
                    sql+='GROUP BY interval_alias '
                    sql+='ORDER BY interval_alias'
                else:
                    sql='SELECT avg(med_valor) as valor, '
                    sql+='to_timestamp(floor((extract(\'epoch\' '
                    sql+='from med_fecha) / 300 )) * 300)'
                    sql+='AT TIME ZONE \'UTC5\' as interval_alias '
                    sql+='FROM '+tabla+ ' WHERE '
                    sql+='est_id_id='+str(estacion.est_id)+ ' and '
                    sql+='med_fecha>=\''+str(fecha_inicio)+'\' and '
                    sql+='med_fecha<=\''+str(fecha_fin)+'\' 23:59:59'
                    sql+='GROUP BY interval_alias '
                    sql+='ORDER BY interval_alias'
                cursor.execute(sql)
            else:
                range_year=range(int(year_ini),int(year_fin)+1)
                consulta=[]
                for year in range_year:
                    tabla=var_cod+'.m'+str(year)
                    if str(year)==year_ini:
                        sql='SELECT * FROM '+tabla+ ' WHERE '
                        sql+='est_id_id='+str(estacion.est_id)+ ' and '
                        sql+='med_fecha>=\''+str(fecha_inicio)+'\' order by med_fecha'
                    elif str(year)==year_fin:
                        sql='SELECT * FROM '+tabla+ ' WHERE '
                        sql+='est_id_id='+str(estacion.est_id)+ ' and '
                        sql+='med_fecha<=\''+str(fecha_fin)+' 23:59:59 \' order by med_fecha'
                    else:
                        sql='SELECT * FROM '+tabla+ ' WHERE '
                        sql+='est_id_id='+str(estacion.est_id)+' order by med_fecha'
                    consulta.extend(list(Medicion.objects.raw(sql)))
            datos=self.dictfetchall(cursor)
        #frecuencia horaria
        elif(frecuencia==str(2)):
            consulta=consulta.annotate(year=ExtractYear('med_fecha'),
                month=ExtractMonth('med_fecha'),
                day=ExtractDay('med_fecha'),
                hour=ExtractHour('med_hora')
            ).values('year','month','day','hour')
            if(variable==str(1)):
                datos=list(consulta.annotate(valor=Sum('med_valor')).
                values('valor','year','month','day','hour').
                order_by('year','month','day','hour'))
            else:
                datos=list(consulta.annotate(valor=Avg('med_valor'),
                maximo=Max('med_maximo'),minimo=Min('med_minimo')).
                values('valor','maximo','minimo','year','month','day','hour').
                order_by('year','month','day','hour'))

        #frecuencia diaria
        elif(frecuencia==str(3)):
            consulta=consulta.annotate(
                year=ExtractYear('med_fecha'),
                month=ExtractMonth('med_fecha'),
                day=ExtractDay('med_fecha')
            ).values('year','month','day')
            if(variable==str(1)):
                datos=list(consulta.annotate(valor=Sum('med_valor')).
                values('valor','year','month','day').
                order_by('year','month','day'))
            else:
                datos=list(consulta.annotate(valor=Avg('med_valor'),
                maximo=Max('med_maximo'),minimo=Min('med_minimo')).
                values('valor','maximo','minimo','year','month','day').
                order_by('year','month','day'))

        #frecuencia mensual
        else:
            consulta=consulta.annotate(
                year=ExtractYear('med_fecha'),
                month=ExtractMonth('med_fecha')
            ).values('month','year')
            if(variable==str(1)):
                consulta=list(consulta.annotate(valor=Sum('med_valor')).
                values('valor','month','year').
                order_by('year','month'))
            else:
                consulta=list(consulta.annotate(valor=Avg('med_valor'),
                maximo=Max('med_maximo'),minimo=Min('med_minimo')).
                values('valor','maximo','minimo','month','year').
                order_by('year','month'))

        return datos
    def dictfetchall(self,cursor):
        #Return all rows from a cursor as a dict
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
