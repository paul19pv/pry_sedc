# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-19 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='sen_codigo',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sen_nombre',
            field=models.CharField(choices=[('Term\xf3metro', 'Term\xf3metro'), ('Higr\xf3metro', 'Higr\xf3metro'), ('Pluvi\xf3grafo', 'Pluvi\xf3grafo'), ('Veleta', 'Veleta'), ('Anem\xf3metro', 'Anem\xf3metro'), ('Bar\xf3metro', 'Bar\xf3metro'), ('TDR', 'TDR'), ('Piran\xf3metro', 'Piran\xf3metro'), ('Term\xf3metro de agua', 'Term\xf3metro de agua'), ('Sensor de nivel', 'Sensor de nivel')], max_length=40, verbose_name='Nombre'),
        ),
    ]