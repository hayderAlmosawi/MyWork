# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-08 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_auto_20160306_0027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Subject',
        ),
        migrations.RenameModel(
            old_name='Teacher_Course',
            new_name='Teacher_Subject',
        ),
        migrations.RenameField(
            model_name='marks',
            old_name='CourseName',
            new_name='SubjectName',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Department',
            new_name='Department_ID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Marks',
            new_name='Marks_ID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Course',
            new_name='Subject_ID',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='CourseDate',
            new_name='SubjectDate',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='CourseName',
            new_name='SubjectName',
        ),
        migrations.RenameField(
            model_name='teacher_subject',
            old_name='Course',
            new_name='Subject',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Research',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='college.ScientificResearch'),
        ),
    ]