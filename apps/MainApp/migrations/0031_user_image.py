# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-03 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0030_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='ProfileImage'),
        ),
    ]
