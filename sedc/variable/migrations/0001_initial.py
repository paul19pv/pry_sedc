# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estacion', '0001_initial'),
        ('datalogger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('con_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('con_fecha_ini', models.DateField(verbose_name='Fecha inicio')),
                ('con_fecha_fin', models.DateField(verbose_name='Fecha fin',blank=True, null=True)),
                ('con_estado', models.BooleanField(default=True, verbose_name='Activo')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                to='estacion.Estacion', verbose_name='Estacion')),
            ],

        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('uni_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('uni_nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('uni_sigla', models.CharField(max_length=10, verbose_name='Sigla')),
            ],
            options={
                'ordering': ('est_id', 'var_id'),
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('var_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('var_codigo', models.CharField(max_length=6, verbose_name='Codigo')),
                ('var_nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('var_maximo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Maximo')),
                ('var_minimo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Minimo')),
                ('var_sos', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Sospechoso',null=True,blank=True)),
                ('var_err', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Error',null=True,blank=True)),
                ('var_min', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Error minimo',null=True,blank=True)),
                ('var_estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('uni_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='variable.Unidad', verbose_name='Unidad')),
            ],
        ),
        migrations.AddField(
            model_name='control',
            name='var_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='variable.Variable', verbose_name='Variable'),
        ),
    ]
