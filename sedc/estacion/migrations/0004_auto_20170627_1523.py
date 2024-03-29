# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacion', '0003_auto_20170627_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='est_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='reg_fecha',
            field=models.DateField(null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='reg_ubicacion',
            field=models.CharField(max_length=200, null=True, verbose_name='Ubicaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='vacios',
            name='est_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='vacios',
            name='vac_observacion',
            field=models.TextField(null=True, verbose_name='Observaci\xf3n'),
        ),
    ]
