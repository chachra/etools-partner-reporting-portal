# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-20 00:01
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0008_auto_20170613_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatorreport',
            name='total',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'c': None, 'd': None, 'v': 0}),
        ),
        migrations.AlterField(
            model_name='reportable',
            name='total',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={'c': None, 'd': None, 'v': 0}),
        ),
    ]
