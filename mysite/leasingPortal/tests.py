import datetime

from django.core.urlresolvers import reverse 
from django.test import TestCase
from django.utils import timezone

from .models import Building, Suite

def create_building(address):
	return Building.objects.create(address=address)

def create_suite(parent, number, available):
	date = datetime.datetime(available[0], available[1], available[2]).date()
	return Suite.objects.create(parent_building=parent, number=number, 
		     date_available=date)

