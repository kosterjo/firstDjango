# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingPortal', '0002_auto_20160701_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suite',
            name='min_lease_term',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='suite',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
