# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estacion', '0001_initial'),
        ('variable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicion',
            fields=[
                ('med_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('med_fecha', models.DateField()),
                ('med_hora', models.TimeField()),
                ('med_valor', models.DecimalField(decimal_places=8, max_digits=18, verbose_name='Valor')),
                ('med_maximo', models.DecimalField(decimal_places=8, max_digits=18, verbose_name='Maximo')),
                ('med_minimo', models.DecimalField(decimal_places=8, max_digits=18, verbose_name='Minimo')),
                ('med_validado', models.DecimalField(decimal_places=8, max_digits=18, verbose_name='Validado')),
                ('med_estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estacion')),
                ('var_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='variable.Variable', verbose_name='Variable')),
            ],
        ),
        migrations.CreateModel(
            name='Validacion',
            fields=[
                ('val_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('val_fecha', models.DateField()),
                ('val_hora', models.TimeField()),
                ('val_valor', models.DecimalField(decimal_places=8, max_digits=18, verbose_name='Valor')),
                ('val_maximo', models.DecimalField(decimal_places=8, max_digits=18, verbose_name='Maximo')),
                ('val_minimo', models.DecimalField(decimal_places=8, max_digits=18, verbose_name='Minimo')),
                ('val_mensaje', models.CharField(max_length=100, verbose_name='Validado')),
                ('med_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='medicion.Medicion', verbose_name='Medicion')),
            ],
        ),
    ]