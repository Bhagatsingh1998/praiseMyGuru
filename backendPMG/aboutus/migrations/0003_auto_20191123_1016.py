# Generated by Django 2.2.7 on 2019-11-23 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0002_auto_20191123_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='dateTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 23, 10, 16, 25, 338370)),
        ),
    ]
