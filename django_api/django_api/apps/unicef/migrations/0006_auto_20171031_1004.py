# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicef', '0005_auto_20171030_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=255, verbose_name='Email'),
        ),
    ]
