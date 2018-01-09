# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-22 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacion', '0007_auto_20170705_1645'),
        ('formato', '0013_auto_20170821_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clasificacion',
            options={'ordering': ('var_id',)},
        ),
        migrations.AlterModelOptions(
            name='formato',
            options={'ordering': ('for_nombre',)},
        ),
        migrations.RemoveField(
            model_name='asociacion',
            name='dat_id',
        ),
        migrations.AddField(
            model_name='asociacion',
            name='est_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='clasificacion',
            name='cla_maximo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Columna valor m\xe1ximo'),
        ),
        migrations.AlterField(
            model_name='clasificacion',
            name='cla_minimo',
            field=models.IntegerField(blank=True, null=True, verbose_name='Columna valor m\xednimo'),
        ),
    ]
