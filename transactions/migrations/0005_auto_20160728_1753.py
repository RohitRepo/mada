# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20160728_1746'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='completed_drop',
            new_name='CompletedDrop',
        ),
    ]
