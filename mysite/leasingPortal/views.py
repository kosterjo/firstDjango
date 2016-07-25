from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.select_template(['leasingPortal/index.html',
		                                'leasingPortal/base.html'])
	return HttpResponse(template.render(request))

def buildings(request, number):
	return HttpResponse('Hey you chose %s.' % number)

def suites(request, number):
	response = 'Shes at least a %s'
	return HttpResponse(response % number)
