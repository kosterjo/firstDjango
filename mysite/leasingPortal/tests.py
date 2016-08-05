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

class BuildingViewTests(TestCase):

	def test_buildings_view_with_no_buildings(self):
		'''
		If no buildings exist, appropriate message should be displayed
		'''
		response = self.client.get(reverse('leasingPortal:buildings'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "you haven't uploaded a building yet!")
		self.assertQuerysetEqual(response.context['building_list'], [])

	def test_buildings_view_with_buildings(self):
		'''
		if buildings exist, no message should be displayed
		'''
		create_building("new_building")
		response = self.client.get(reverse('leasingPortal:buildings',))
		self.assertEqual(response.status_code, 200)
		self.assertNotContains(response, "you haven't uploaded a building yet!")
		self.assertQuerysetEqual(response.context['building_list'], 
		                         ['<Building: new_building>'])

	def test_building_details_view_without_suites(self):
		'''
		if building has no children suites, an appropriate message 
		should be displayed
		'''
		building = create_building("new_building")
		url      = reverse('leasingPortal:building_detail', args=(building.id,))
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "you haven't uploaded a suite yet!")
		self.assertQuerysetEqual(response.context['suite_list'], [])

	def test_building_details_view_with_suites(self):
		'''
		if building has children suites, no message should be displayed
		'''
		building = create_building("new_building")
		create_suite(building, 1, [2016, 8, 5])

		url      = reverse('leasingPortal:building_detail', args=(building.id,))
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertNotContains(response, "you haven't uploaded a suite yet!")
		self.assertQuerysetEqual(response.context['suite_list'], 
		                         ['<Suite: Suite #1>'])

	def test_building_details_view_with_bastard_suites(self):
		'''
		if building has children suites, no message should be displayed
		'''
		building  = create_building("new_building")
		building2 = create_building("newer_building")

		create_suite(building, 1, [2016, 8, 5])
		create_suite(building2, 2, [2016, 8, 5])

		url      = reverse('leasingPortal:building_detail', args=(building.id,))
		response = self.client.get(url)

		self.assertEqual(response.status_code, 200)
		self.assertNotContains(response, "you haven't uploaded a suite yet!")
		self.assertQuerysetEqual(response.context['suite_list'], 
		                         ['<Suite: Suite #1>'])