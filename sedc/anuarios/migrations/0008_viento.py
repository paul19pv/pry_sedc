# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacion', '0007_auto_20170705_1645'),
        ('anuarios', '0007_radiacionsolar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viento',
            fields=[
                ('vie_id', models.AutoField(primary_key=True, serialize=False)),
                ('vie_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('vie_mes', models.IntegerField(verbose_name='Mes')),
                ('vie_direccion', models.CharField(max_length=10, verbose_name='Direcci\xf3n')),
                ('vie_promedio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Promdio')),
                ('vie_porcentaje', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Porcentaje')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
        ),
    ]
