# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicion', '0005_auto_20170710_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicion',
            name='med_valor',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=14, null=True, verbose_name='Valor'),
        ),
    ]
