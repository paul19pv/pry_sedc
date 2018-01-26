# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formato', '0021_fecha_hora'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fecha',
            options={'ordering': ('fec_id',)},
        ),
        migrations.AlterModelOptions(
            name='hora',
            options={'ordering': ('hor_id',)},
        ),
        migrations.AddField(
            model_name='formato',
            name='fec_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='formato.Fecha', verbose_name='Formato de Fecha1'),
        ),
        migrations.AddField(
            model_name='formato',
            name='hor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='formato.Hora', verbose_name='Formato de Hora1'),
        ),
    ]