# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalogger', '0004_remove_sensor_sen_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sen_marca',
            field=models.CharField(choices=[('CAMPBELL', 'CAMPBELL'), ('VAISALA', 'VAISALA'), ('YOUNG', 'YOUNG'), ('APOGEE', 'APOGEE'), ('TEXAS ELECTRONICS', 'TEXAS ELECTRONICS'), ('HOBO', 'HOBO')], max_length=20, null=True, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sen_nombre',
            field=models.CharField(choices=[('Term\xf3metro', 'Term\xf3metro'), ('Higr\xf3metro', 'Higr\xf3metro'), ('Pluvi\xf3grafo', 'Pluvi\xf3grafo'), ('Veleta', 'Veleta'), ('Anem\xf3metro', 'Anem\xf3metro'), ('Bar\xf3metro', 'Bar\xf3metro'), ('TDR', 'TDR'), ('Piran\xf3metro', 'Piran\xf3metro')], max_length=20, verbose_name='Nombre'),
        ),
    ]
