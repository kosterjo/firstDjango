from datetime import datetime

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import Building, Suite

def index(request):
	return render(request, 'leasingPortal/index.html')

def buildings(request):
	building_list = Building.objects.all()
	all_suites = []

	for building in building_list:
		all_suites.append(Suite.objects.filter(parent_building=building.id))

	buildings_and_suites = zip(building_list, all_suites)

	context = {
	  'buildings_and_suites': buildings_and_suites
	}

	return render(request, 'leasingPortal/buildings.html', context)

def building_edit(request, building_id):
	building = get_object_or_404(Building, pk=building_id)
	context = {
	  'building': building,
	}

	return render(request, 'leasingPortal/buildingEdit.html', context)

def post_building_edit(request, building_id):
	building = get_object_or_404(Building, pk=building_id)

	if not (request.POST['address']):
		return render(request, 'leasingPortal/buildingEdit.html', {
    'building': building, 
    'error_message': "building address cannot be blank",
	})
	else: 
		building.address = request.POST['address']
		building.save()
		return HttpResponseRedirect(reverse('leasingPortal:buildings', kwargs={}))

def add_suite(request, building_id):
	context = {
	  'building_id': building_id,
	}

	return render(request, 'leasingPortal/addSuite.html', context)

def post_add_suite(request, building_id):
	building = get_object_or_404(Building, pk=building_id)

	if not (request.POST['number']):
		return render(request, 'leasingPortal/addSuite.html', {
	    'building_id': building_id, 
	    'error_message': "you didn't enter a suite number",
		})

	if not (request.POST['available']):
		return render(request, 'leasingPortal/addSuite.html', {
	    'building_id':   building_id, 
	    'error_message': "you didn't enter an availability date",
		}) 	

	else: 
		number      = request.POST['number']
		date        = str(request.POST['available'])
		date_parsed = date[6:] + '-' + date[:-8] + '-' + date[3:-5]
		s           = Suite(parent_building=building, number=number,
		              date_available=date_parsed)
		s.save()

		return HttpResponseRedirect(reverse('leasingPortal:buildings', kwargs={}))

def edit_suite(request, building_id, suite_id):
	suite = get_object_or_404(Suite, pk=suite_id)
	context = {
	  'building_id': building_id,
	  'suite':       suite
	}

	return render(request, 'leasingPortal/editSuite.html', context)

def post_edit_suite(request, building_id, suite_id):
	suite       = get_object_or_404(Suite, pk=suite_id)
	number      = request.POST['number']
	date        = str(request.POST['available'])

	if number:
		suite.number = number

	if date:
		date_parsed = date[6:] + '-' + date[:-8] + '-' + date[3:-5]
		suite.date_available = date_parsed

	suite.save()
	return HttpResponseRedirect(reverse('leasingPortal:buildings', kwargs={}))