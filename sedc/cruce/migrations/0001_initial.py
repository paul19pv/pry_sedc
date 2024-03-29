# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 12:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estacion', '0007_auto_20170705_1645'),
        ('variable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruce',
            fields=[
                ('cru_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('est_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estacion.Estacion', verbose_name='Estaci\xf3n')),
                ('var_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='variable.Variable', verbose_name='Variable')),
            ],
            options={
                'ordering': ('cru_id', 'est_id', 'var_id'),
            },
        ),
    ]
