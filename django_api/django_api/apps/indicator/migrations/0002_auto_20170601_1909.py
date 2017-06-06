# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-01 19:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatorreport',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2017, 6, 1, 19, 9, 27, 447768, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indicatorreport',
            name='submission_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of submission'),
        ),
    ]