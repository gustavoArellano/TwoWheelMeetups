# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-05-22 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_auto_20190522_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='EventTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]