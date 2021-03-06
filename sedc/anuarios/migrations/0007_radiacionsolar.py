# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-21 10:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacion', '0007_auto_20170705_1645'),
        ('anuarios', '0006_caudal_humedadsuelo_nivelagua_presionatmosferica_temperaturaagua'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadiacionSolar',
            fields=[
                ('rad_id', models.AutoField(primary_key=True, serialize=False)),
                ('rad_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('rad_mes', models.IntegerField(verbose_name='Mes')),
                ('rad_hora', models.IntegerField(verbose_name='Hora')),
                ('rad_maximo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xe1ximo')),
                ('rad_minimo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xednimo')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
        ),
    ]
