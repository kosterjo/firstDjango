# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-05 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingPortal', '0007_auto_20160804_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suite',
            name='date_available',
            field=models.DateField(null=True),
        ),
    ]
