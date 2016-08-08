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
		all_suites.append( Suite.objects.filter(parent_building=building.id))

	context = {
	  'building_list': building_list,
	  'all_suites': all_suites,
	}

	return render(request, 'leasingPortal/buildings.html', context)

def building_detail(request, building_id):
	building = get_object_or_404(Building, pk=building_id)
	suite_list = Suite.objects.filter(parent_building=building.id)
	context = {
	  'building': building,
	  'suite_list': suite_list,
	}

	return render(request, 'leasingPortal/buildingDetail.html', context )

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
		return HttpResponseRedirect(reverse('leasingPortal:building_edit', args=(building_id,)))

def add_suite(request, building_id):
	building = get_object_or_404(Building, pk=building_id)
	suite_list = Suite.objects.filter(parent_building=building.id) 

	if not (request.POST['number']):
		return render(request, 'leasingPortal/buildingDetail.html', {
	    'building': building, 
	    'error_message': "you didn't enter a suite number",
	    'suite_list': suite_list
		})

	if not (request.POST['available']):
		return render(request, 'leasingPortal/buildingDetail.html', {
	    'building': building, 
	    'error_message': "you didn't enter an availability date",
	    'suite_list': suite_list,
		}) 	

	else: 
		number      = request.POST['number']
		date        = str(request.POST['available'])
		date_parsed = date[6:] + '-' + date[:-8] + '-' + date[3:-5]
		s           = Suite(parent_building=building, number=number,
		              date_available=date_parsed)
		s.save()

		return HttpResponseRedirect(reverse('leasingPortal:building_detail', args=(building_id,)))