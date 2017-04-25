# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20170422_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='watched',
            field=models.BooleanField(default=False),
        ),
    ]