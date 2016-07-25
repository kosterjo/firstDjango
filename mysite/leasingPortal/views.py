from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Building

def index(request):
	building_list = Building.objects.order_by('address')
	template = loader.select_template(['leasingPortal/index.html',
		                                'leasingPortal/base.html'])
	context = {
	  'building_list': building_list,
	}
	return HttpResponse(template.render(context, request))

def buildings(request, number):
	return HttpResponse('Hey you chose %s.' % number)

def suites(request, number):
	response = 'Shes at least a %s'
	return HttpResponse(response % number)
