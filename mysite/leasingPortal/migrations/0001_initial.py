# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('notes', models.TextField()),
                ('date_available', models.DateTimeField()),
                ('access', models.TextField()),
                ('available', models.BooleanField()),
                ('extra_net_costs', models.DecimalField(decimal_places=2, max_digits=3)),
                ('min_lease_term', models.IntegerField()),
                ('rental_rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('size', models.IntegerField()),
                ('last_modified', models.DateField()),
                ('parent_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leasingPortal.Building')),
            ],
        ),
    ]