# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-07 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestration', '0019_remove_project_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
