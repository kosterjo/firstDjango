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
	parent_building = models.ForeignKey(Building, on_delete=models.CASCADE)
	number          = models.IntegerField()
	date_available  = models.DateField(null = True)
	modified        = ModificationDateTimeField()

	def __str__(self):
		return "Suite #" + str(self.number)
