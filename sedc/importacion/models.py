# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils import timezone
from estacion.models import Estacion
from formato.models import Formato
from datetime import date

class Importacion(models.Model):
    imp_id=models.AutoField("Id",primary_key=True)
    est_id=models.ForeignKey(
    	Estacion,
    	models.SET_NULL,
    	blank=True,
    	null=True,
    	verbose_name="Estación")
    for_id=models.ForeignKey(
        Formato,
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Formato"
    )
    imp_fecha=models.DateField("Fecha",default=date.today)
    imp_hora=models.TimeField("Hora",default=date.today().strftime("%H:%M:%S"))
    imp_archivo=models.CharField("Archivo",max_length=100)
    def get_absolute_url(self):
        return reverse('importacion:importacion_detail', kwargs={'pk': self.pk})