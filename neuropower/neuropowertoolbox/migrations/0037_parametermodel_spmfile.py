# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuropowertoolbox', '0036_parametermodel_maskfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametermodel',
            name='spmfile',
            field=models.FileField(default='', upload_to='maps'),
        ),
    ]
