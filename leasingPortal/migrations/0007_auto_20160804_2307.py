# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leasingPortal', '0006_auto_20160702_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suite',
            name='access',
        ),
        migrations.RemoveField(
            model_name='suite',
            name='available',
        ),
        migrations.RemoveField(
            model_name='suite',
            name='extra_net_costs',
        ),
        migrations.RemoveField(
            model_name='suite',
            name='min_lease_term',
        ),
        migrations.RemoveField(
            model_name='suite',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='suite',
            name='rental_rate',
        ),
        migrations.RemoveField(
            model_name='suite',
            name='size',
        ),
    ]
