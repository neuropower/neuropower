# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-17 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0025_designmodel_nestpars'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='stim_duration',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
    ]
