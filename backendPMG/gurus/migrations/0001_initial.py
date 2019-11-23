# Generated by Django 2.2.7 on 2019-11-23 10:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20191123_1009'),
        ('add', '0004_auto_20191123_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Praise',
            fields=[
                ('teacherID', models.AutoField(primary_key=True, serialize=False)),
                ('worthListening', models.IntegerField()),
                ('starts', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1)),
                ('subjects', multiselectfield.db.fields.MultiSelectField(choices=[('civil', 'civil'), ('compuer organization', 'compuer organization'), ('data structures', 'data structures'), ('mathematics', 'mathematics'), ('chemistry', 'chemistry'), ('electrical', 'electrical'), ('at&c', 'at&c'), ('networking', 'networking'), ('dotnet', 'dotnet'), ('software engineering', 'software engineering'), ('algorthiums', 'algorthiums'), ('c', 'c'), ('physics', 'physics'), ('mechnical', 'mechnical'), ('electronics', 'electronics'), ('java', 'java'), ('management fot it', 'management fot it'), ('dbms', 'dbms')], max_length=191)),
                ('tags', multiselectfield.db.fields.MultiSelectField(choices=[('Respected', 'Respected'), ('Gives Homework', 'Gives Homework'), ('Accessible Outside Class', 'Accessible Outside Class'), ('Participation Matters', 'Participation Matters'), ('Can Skip Class Easily', 'Can Skip Class Easily'), ('Fluttershy', 'Fluttershy'), ('Inspirational', 'Inspirational'), ('Test Heavy', 'Test Heavy'), ('Group Projects', 'Group Projects'), ('Clear Grading Criteria', 'Clear Grading Criteria'), ('Hilarious', 'Hilarious'), ('Beware Of Pop Quizzers', 'Beware Of Pop Quizzers'), ('Amazing Lectures', 'Amazing Lectures'), ('Lecture Heavy', 'Lecture Heavy'), ('Caring', 'Caring'), ('Extra Credit', 'Extra Credit'), ('Tough Grader', 'Tough Grader'), ('Have to write notes', 'Have to write notes')], max_length=284)),
                ('suggest', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=1)),
                ('suggestion', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime(2019, 11, 23, 10, 8, 26, 708468))),
                ('addteacherID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='add.AddTeacher')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.Signups')),
            ],
        ),
    ]
