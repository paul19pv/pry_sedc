# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datalogger', '0002_datalogger_est_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datalogger',
            name='dat_nombre',
        ),
    ]
