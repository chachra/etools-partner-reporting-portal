# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster',
            name='user',
        ),
    ]