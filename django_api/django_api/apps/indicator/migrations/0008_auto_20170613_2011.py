# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-13 20:11
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicator', '0007_remove_indicatorreport_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatorlocationdata',
            name='disaggregation_reported_on',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None),
        ),
        migrations.AddField(
            model_name='indicatorlocationdata',
            name='level_reported',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indicatorlocationdata',
            name='num_disaggregation',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
