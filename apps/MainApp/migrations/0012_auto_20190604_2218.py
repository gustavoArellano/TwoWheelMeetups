# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-04 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_event_usergoing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='UserGoing',
            field=models.ManyToManyField(to='MainApp.User'),
        ),
    ]
