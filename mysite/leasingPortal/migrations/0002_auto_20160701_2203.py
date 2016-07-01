# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasingPortal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suite',
            name='extra_net_costs',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='suite',
            name='min_lease_term',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='suite',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
