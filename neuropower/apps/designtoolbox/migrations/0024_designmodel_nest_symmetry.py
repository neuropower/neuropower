# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-15 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designtoolbox', '0023_auto_20160915_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='designmodel',
            name='nest_symmetry',
            field=models.BooleanField(default=False),
        ),
    ]
