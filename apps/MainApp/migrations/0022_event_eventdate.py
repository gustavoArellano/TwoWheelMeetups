# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-01 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0021_remove_event_eventdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='EventDate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
