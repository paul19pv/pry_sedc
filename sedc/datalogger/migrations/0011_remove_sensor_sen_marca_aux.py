# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-21 12:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datalogger', '0010_sensor_sen_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='sen_marca_aux',
        ),
    ]
