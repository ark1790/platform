# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-09-28 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_auto_20170701_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
