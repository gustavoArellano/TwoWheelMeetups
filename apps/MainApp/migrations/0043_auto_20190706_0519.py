# Generated by Django 2.2.3 on 2019-07-06 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0042_auto_20190706_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Users/gustavo/Documents/Projects/Python/TwoWheelMeetups/apps/MainApp/media/RiderImages'),
        ),
    ]
