# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-04 22:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0012_auto_20190604_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='UserGoing',
            new_name='UsersGoing',
        ),
    ]
