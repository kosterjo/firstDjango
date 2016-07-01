from __future__ import unicode_literals

from django.db import models
from django import forms

class Building(models.Model):
	address = models.CharField(max_length=200)

class Suite(models.Model):
	parent_building = models.ForeignKey(Building, on_delete=models.CASCADE)
	number          = models.IntegerField()
	notes           = models.TextField()
	date_available  = models.DateTimeField()
	access          = models.TextField()
	annually        = forms.ChoiceField(choices=['annually', 'monthly'])
	available       = models.BooleanField()
	extra_net_costs = models.DecimalField(max_digits = 3, decimal_places = 2)
	payment_type    = forms.ChoiceField(choices=['MG', 'FSG', 'NNN'])
	min_lease_term  = models.IntegerField()
	rental_rate     = models.DecimalField(max_digits = 3, decimal_places = 2)
	size            = models.IntegerField()
	last_modified   = models.DateField()
