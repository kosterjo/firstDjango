# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingPortal', '0004_remove_suite_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suite',
            name='date_available',
            field=models.DateTimeField(null=True),
        ),
    ]
