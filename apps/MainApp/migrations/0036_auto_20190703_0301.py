# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-03 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0035_auto_20190703_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='RiderImage',
            field=models.ImageField(blank=True, upload_to='/media/'),
        ),
    ]
