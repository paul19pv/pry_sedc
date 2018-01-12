# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formato', '0002_auto_20170612_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociacion',
            name='est_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='clasificacion',
            name='cla_maximo',
            field=models.IntegerField(verbose_name='M\xe1ximo valor de clasificaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='clasificacion',
            name='cla_minimo',
            field=models.IntegerField(verbose_name='M\xednimo valor de clasificaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='clasificacion',
            name='cla_valor',
            field=models.IntegerField(verbose_name='Valor de clasificaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='formato',
            name='ext_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='formato.Extension', verbose_name='Extensi\xf3n'),
        ),
        migrations.AlterField(
            model_name='formato',
            name='for_col_fecha',
            field=models.IntegerField(verbose_name='Columna fecha'),
        ),
        migrations.AlterField(
            model_name='formato',
            name='for_col_hora',
            field=models.IntegerField(verbose_name='Columna de hora'),
        ),
        migrations.AlterField(
            model_name='formato',
            name='for_fecha',
            field=models.CharField(max_length=12, verbose_name='Formato de fecha'),
        ),
        migrations.AlterField(
            model_name='formato',
            name='for_fil_ini',
            field=models.IntegerField(verbose_name='Fila de inicio'),
        ),
        migrations.AlterField(
            model_name='formato',
            name='for_hora',
            field=models.CharField(max_length=10, verbose_name='Formato de hora'),
        ),
        migrations.AlterField(
            model_name='formato',
            name='for_num_col',
            field=models.IntegerField(verbose_name='N\xfamero de columnas'),
        ),
    ]