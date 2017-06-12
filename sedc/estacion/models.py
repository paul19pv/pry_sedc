# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from formato.models import Formato

# Create your models here.
class Estacion(models.Model):
    TIPO_ESTACION=(
        ('M','Meteorológica'),
	('P','Pluviométrica'),
        ('H','Hidrológica'),
    )
    est_id=models.AutoField("Id",primary_key=True)
    est_codigo=models.CharField("Código",max_length=10)
    est_nombre=models.CharField("Nombre",max_length=100)
    est_tipo=models.CharField("Tipo",max_length=25,choices=TIPO_ESTACION)
    est_estado=models.BooleanField(default=True)
    est_provincia=models.CharField("Provincia",max_length=50,null=True)
    est_latitud=models.CharField("Latitud",max_length=12,null=True)
    est_longitud=models.CharField("Longitud",max_length=12,null=True)
    est_altura=models.IntegerField("Altura",null=True)
    est_ficha=models.FileField(upload_to='fichas/')
class Vacios(models.Model):
    vac_id=models.AutoField("Id",primary_key=True)
    est_id=models.ForeignKey(
	Estacion,
	models.SET_NULL,
	blank=True,
	null=True, 
	verbose_name="Estacion")
    vac_fecha_ini=models.DateField()
    vac_fecha_fin=models.DateField()
    vac_observacion=models.TextField("Observacion",null=True)
class Registro(models.Model):
    reg_id=models.AutoField("Id",primary_key=True)
    est_id=models.ForeignKey(
	Estacion, 
	models.SET_NULL, 
	blank=True, 
	null=True, 
	verbose_name="Estacion")

