# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 22:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasingPortal', '0003_auto_20160701_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suite',
            name='last_modified',
        ),
    ]
