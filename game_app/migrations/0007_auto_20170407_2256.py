# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 22:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0006_game_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='date',
            field=models.DateField(default=datetime.date(2017, 4, 7)),
        ),
    ]
