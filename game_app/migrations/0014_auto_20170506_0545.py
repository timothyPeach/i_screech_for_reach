# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-06 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0013_auto_20170506_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='rank',
            field=models.CharField(default='', max_length=14),
        ),
    ]
