import datetime

from django.core.urlresolvers import reverse 
from django.test import TestCase
from django.utils import timezone

from .models import Building

def create_building(address):
	return Building.objects.create(address=address)


