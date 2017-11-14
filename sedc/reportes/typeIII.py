# -*- coding: utf-8 -*-
import plotly.offline as opy
import plotly.graph_objs as go
from reportes.titulos import Titulos
from anuarios.models import TemperaturaAire
#clase para anuario de la variable TAI
class TypeIII(Titulos):

    def consulta(self,estacion,periodo):
        #annotate agrupa los valores en base a un campo y a una operacion
        informacion=list (TemperaturaAire.objects.filter(est_id=estacion).filter(tai_periodo=periodo))
        return informacion
    def matriz(self,estacion, variable, periodo):
        datos=self.consulta(estacion,periodo)
        return datos
    def grafico(self,estacion, variable, periodo):
        datos=self.consulta(estacion,periodo)
        meses=[]
        max_simple=[]
        min_simple=[]
        avg_simple=[]
        for item in datos:
            meses.append(item.tai_mes)
            max_simple.append(item.tai_maximo)
            min_simple.append(item.tai_minimo)
            avg_simple.append(item.tai_promedio)
            
        trace0 = go.Scatter(
            x = meses,
            y = max_simple,
            name = 'Max',
            line = dict(
                color = ('rgb(22, 96, 167)'),
                width = 4)
        )
        trace1 = go.Scatter(
            x = meses,
            y = min_simple,
            name = 'Min',
            line = dict(
                color = ('rgb(205, 12, 24)'),
                width = 4,)
        )
        trace2 = go.Scatter(
            x = meses,
            y = avg_simple,
            name = 'Media',
            line = dict(
                color = ('rgb(50, 205, 50)'),
                width = 4,)
        )
        data = go.Data([trace0, trace1, trace2])
        layout = go.Layout(title = str(self.titulo_grafico(variable)) + str(" (") + str(self.titulo_unidad(variable)) + str(")"))
        figure = go.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')
        return div
