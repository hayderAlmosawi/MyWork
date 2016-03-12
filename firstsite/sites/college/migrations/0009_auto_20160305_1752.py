# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0008_marks_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=50)),
                ('CourseDate', models.DateField()),
                ('ClassRoomNumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepartmentName', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='object',
            new_name='CourseName',
        ),
    ]
