# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unicef', '0008_auto_20171031_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdresultlink',
            name='title',
            field=models.CharField(max_length=512, verbose_name='CP output title/name'),
        ),
    ]
