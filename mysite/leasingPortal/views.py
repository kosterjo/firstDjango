from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('leasingPortal/index.html')
	return HttpResponse(template.render(request))

def buildings(request, number):
	return HttpResponse('Hey you chose %s.' % number)

def suites(request, number):
	response = 'Shes at least a %s'
	return HttpResponse(response % number)
