# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20170929_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='travel',
            old_name='users',
            new_name='user',
        ),
    ]
