# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-22 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datalogger', '0018_remove_datalogger_dat_marca_aux'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='sen_marca',
            new_name='mar_id',
        ),
    ]