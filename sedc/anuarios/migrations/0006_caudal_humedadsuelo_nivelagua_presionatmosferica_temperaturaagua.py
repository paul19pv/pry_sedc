# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-19 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacion', '0007_auto_20170705_1645'),
        ('anuarios', '0005_auto_20170918_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caudal',
            fields=[
                ('cau_id', models.AutoField(primary_key=True, serialize=False)),
                ('cau_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('cau_mes', models.IntegerField(verbose_name='Mes')),
                ('cau_maximo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xe1ximo')),
                ('cau_minimo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xednimo')),
                ('cau_promedio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Promedio')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
            options={
                'ordering': ('cau_mes',),
            },
        ),
        migrations.CreateModel(
            name='HumedadSuelo',
            fields=[
                ('hsu_id', models.AutoField(primary_key=True, serialize=False)),
                ('hsu_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('hsu_mes', models.IntegerField(verbose_name='Mes')),
                ('hsu_maximo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xe1ximo')),
                ('hsu_minimo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xednimo')),
                ('hsu_promedio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Promedio')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
            options={
                'ordering': ('hsu_mes',),
            },
        ),
        migrations.CreateModel(
            name='NivelAgua',
            fields=[
                ('nag_id', models.AutoField(primary_key=True, serialize=False)),
                ('nag_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('nag_mes', models.IntegerField(verbose_name='Mes')),
                ('nag_maximo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xe1ximo')),
                ('nag_minimo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xednimo')),
                ('nag_promedio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Promedio')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
            options={
                'ordering': ('nag_mes',),
            },
        ),
        migrations.CreateModel(
            name='PresionAtmosferica',
            fields=[
                ('pat_id', models.AutoField(primary_key=True, serialize=False)),
                ('pat_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('pat_mes', models.IntegerField(verbose_name='Mes')),
                ('pat_maximo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xe1ximo')),
                ('pat_minimo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xednimo')),
                ('pat_promedio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Promedio')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
            options={
                'ordering': ('pat_mes',),
            },
        ),
        migrations.CreateModel(
            name='TemperaturaAgua',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_periodo', models.IntegerField(default=2000, verbose_name='A\xf1o')),
                ('tag_mes', models.IntegerField(verbose_name='Mes')),
                ('tag_maximo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xe1ximo')),
                ('tag_minimo', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='M\xednimo')),
                ('tag_promedio', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Promedio')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
            ],
            options={
                'ordering': ('tag_mes',),
            },
        ),
    ]