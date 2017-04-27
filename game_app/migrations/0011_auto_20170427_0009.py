# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-27 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0010_player_bank_ms'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='rank_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='rank_promote',
            field=models.IntegerField(default=45),
        ),
        migrations.AlterField(
            model_name='account',
            name='elo',
            field=models.IntegerField(default=1500),
        ),
        migrations.AlterField(
            model_name='account',
            name='rank',
            field=models.IntegerField(default=-9),
        ),
    ]