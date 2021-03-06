# Generated by Django 2.2.7 on 2019-11-27 17:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=15)),
                ('userName', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('confirmPassword', models.CharField(max_length=15)),
                ('category', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=10)),
                ('agreeTerms', models.BooleanField(default=True)),
                ('dateTime', models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 27, 17, 23, 10, 192976))),
            ],
        ),
        migrations.CreateModel(
            name='Dashbord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=9999)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/post')),
                ('dateTime', models.DateTimeField(verbose_name=datetime.datetime(2019, 11, 27, 17, 23, 10, 209756))),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Signups')),
            ],
        ),
    ]
