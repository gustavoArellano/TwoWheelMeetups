# Generated by Django 2.2.3 on 2019-07-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0040_auto_20190705_0409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Image',
            field=models.ImageField(blank=True, default='/static/MainApp/images/placeholder.png', upload_to='Users/gustavo/Documents/Projects/Python/TwoWheelMeetups/apps/MainApp/media/RiderImages'),
        ),
    ]
