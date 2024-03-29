# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estacion', '0007_auto_20170705_1645'),
        ('variable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('bit_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('bit_fecha_ini', models.DateField(verbose_name='Fecha de inicio')),
                ('bit_fecha_fin', models.DateField(blank=True, null=True, verbose_name='fecha de fin')),
                ('bit_observacion', models.CharField(blank=True, max_length=500, verbose_name='Observacion')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estacion')),
                ('var_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='variable.Variable', verbose_name='Variable')),
            ],
            options={
                'ordering': ('bit_id', 'est_id', 'var_id'),
            },
        ),
    ]
