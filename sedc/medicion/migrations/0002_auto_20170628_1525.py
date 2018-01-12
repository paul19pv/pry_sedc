# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicion',
            name='est_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='med_fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='med_hora',
            field=models.TimeField(verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='med_maximo',
            field=models.DecimalField(decimal_places=6, max_digits=14, verbose_name='M\xe1ximo'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='med_minimo',
            field=models.DecimalField(decimal_places=6, max_digits=14, verbose_name='M\xednimo'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='med_validado',
            field=models.DecimalField(decimal_places=6, max_digits=14, verbose_name='Validado'),
        ),
        migrations.AlterField(
            model_name='medicion',
            name='med_valor',
            field=models.DecimalField(decimal_places=6, max_digits=14, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='validacion',
            name='val_maximo',
            field=models.DecimalField(decimal_places=6, max_digits=14, verbose_name='Maximo'),
        ),
        migrations.AlterField(
            model_name='validacion',
            name='val_minimo',
            field=models.DecimalField(decimal_places=6, max_digits=14, verbose_name='Minimo'),
        ),
        migrations.AlterField(
            model_name='validacion',
            name='val_valor',
            field=models.DecimalField(decimal_places=6, max_digits=14, verbose_name='Valor'),
        ),
    ]