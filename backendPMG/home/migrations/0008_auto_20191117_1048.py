# Generated by Django 2.2.7 on 2019-11-17 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191116_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='try',
            name='pic',
        ),
        migrations.AddField(
            model_name='try',
            name='exp',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
