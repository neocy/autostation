# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestration', '0007_auto_20170822_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='description',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]