# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacion', '0007_auto_20170705_1645'),
        ('anuarios', '0009_auto_20180109_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='DireccionVelocidad',
            fields=[
                ('vie_id', models.AutoField(primary_key=True, serialize=False)),
                ('vie_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('vie_mes', models.IntegerField(verbose_name='Mes')),
                ('vie_direccion', models.CharField(max_length=2, verbose_name='Direcci\xf3n')),
                ('vie_promedio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Velocidad Media por direcci\xf3n')),
                ('vie_porcentaje', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Porcentaje de velocidades medias por direcci\xf3n')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
        ),
        migrations.RemoveField(
            model_name='viento',
            name='est_id',
        ),
        migrations.DeleteModel(
            name='Viento',
        ),
    ]
