from __future__ import unicode_literals

from django.db import models
from django import forms
import django_extensions
from django_extensions.db.fields import ModificationDateTimeField

class Building(models.Model):
	address  = models.CharField(max_length=200)
	modified = ModificationDateTimeField()

	def __str__(self):
		return self.address

class Suite(models.Model):
	pay_choice = (
  	('YR', 'yearly'), 
  	('MO', 'monthly'),
	)

	parent_building = models.ForeignKey(Building, on_delete=models.CASCADE)
	number          = models.IntegerField()
	notes           = models.TextField(null = True, blank = True)
	date_available  = models.DateTimeField(null = True)
	access          = models.TextField()
	#annually        = forms.ChoiceField(choices=pay_choice)
	available       = models.BooleanField()
	extra_net_costs = models.DecimalField(null = True, blank = True, max_digits = 3, decimal_places = 2)
	#payment_type    = forms.ChoiceField(choices=['MG', 'FSG', 'NNN'])
	min_lease_term  = models.IntegerField(null = True, blank = True)
	rental_rate     = models.DecimalField(max_digits = 3, decimal_places = 2)
	size            = models.IntegerField()
	modified        = ModificationDateTimeField()

	def __str__(self):
		return "Suite #" + str(self.number)
