# Generated by Django 2.2.7 on 2019-11-16 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_try_sub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='try',
            name='sub',
        ),
        migrations.AddField(
            model_name='try',
            name='drop',
            field=models.CharField(choices=[('civil', 'civil'), ('compuer organization', 'compuer organization'), ('data structures', 'data structures'), ('mathematics', 'mathematics'), ('chemistry', 'chemistry'), ('electrical', 'electrical'), ('at&c', 'at&c'), ('networking', 'networking'), ('dotnet', 'dotnet'), ('software engineering', 'software engineering'), ('algorthiums', 'algorthiums'), ('c', 'c'), ('physics', 'physics'), ('mechnical', 'mechnical'), ('electronics', 'electronics'), ('java', 'java'), ('management fot it', 'management fot it'), ('dbms', 'dbms')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
