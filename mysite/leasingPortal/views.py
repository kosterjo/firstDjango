from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import Building

def index(request):
	template = loader.select_template(['leasingPortal/index.html',
		                                 'leasingPortal/base.html'])

	return render(request, 'leasingPortal/index.html')

def buildings(request):
	building_list = Building.objects.order_by('address')
	template = loader.select_template(['leasingPortal/buildings.html',
		                                 'leasingPortal/base.html'])
	context = {
	  'building_list': building_list,
	}

	return render(request, 'leasingPortal/buildings.html', context)

def building_detail(request, building_id):
	try:
		building = Building.objects.get(pk=building_id)
	except Building.DoesNotExist:
		raise Http404("Building does not exist")
