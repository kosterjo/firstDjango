from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Building

def index(request):
	building_list = Building.objects.order_by('address')
	template = loader.select_template(['leasingPortal/index.html',
		                                 'leasingPortal/base.html'])
	context = {
	  'building_list': building_list,
	}
	return render(request, 'leasingPortal/index.html', context)

def buildings(request):
	template = loader.select_template(['leasingPortal/buildings.html',
		                                'leasingPortal/base.html'])
	return HttpResponse(template.render(request))

def suites(request, number):
	response = 'Shes at least a %s'
	return HttpResponse(response % number)
