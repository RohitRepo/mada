# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_auto_20160728_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completed',
            name='before_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='before_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='month_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='month_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='week_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='week_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='yesterday_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completed',
            name='yesterday_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='before_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='before_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='month_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='month_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='week_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='week_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='yesterday_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='completeddrop',
            name='yesterday_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='before_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='before_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='month_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='month_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='week_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='week_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='yesterday_dau',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='started',
            name='yesterday_nu',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
