# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-02 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('variable', '0001_initial'),
        ('estacion', '0007_auto_20170705_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Validacion',
            fields=[
                ('val_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('val_fecha', models.DateField(verbose_name='Fecha')),
                ('val_hora', models.TimeField(verbose_name='Hora')),
                ('val_valor', models.DecimalField(blank=True, decimal_places=6, max_digits=14, null=True, verbose_name='Valor')),
                ('val_maximo', models.DecimalField(blank=True, decimal_places=6, max_digits=14, null=True, verbose_name='M\xe1ximo')),
                ('val_minimo', models.DecimalField(blank=True, decimal_places=6, max_digits=14, null=True, verbose_name='M\xednimo')),
                ('val_validado', models.DecimalField(blank=True, decimal_places=6, max_digits=14, null=True, verbose_name='Validado')),
                ('val_estado', models.NullBooleanField(default=True, verbose_name='Estado')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
                ('var_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='variable.Variable', verbose_name='Variable')),
            ],
        ),
    ]
