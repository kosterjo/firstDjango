# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-08 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasingPortal', '0008_auto_20160805_0015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suite',
            name='date_available',
        ),
    ]