# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formato', '0004_auto_20170627_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='delimitador',
            name='del_codigo',
            field=models.IntegerField(null=True, verbose_name='C\xf3digo'),
        ),
    ]
