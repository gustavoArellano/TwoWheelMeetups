# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-03 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0037_auto_20190703_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='RiderImage',
            field=models.ImageField(blank=True, default='/static/MainApp/images/placeholder.png', upload_to='/RiderImages'),
        ),
    ]
