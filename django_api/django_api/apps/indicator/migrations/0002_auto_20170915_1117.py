# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-15 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportable',
            name='end_date',
            field=models.DateField(verbose_name='End Date'),
        ),
    ]
