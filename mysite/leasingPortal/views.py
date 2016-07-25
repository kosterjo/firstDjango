from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<p>Index view</p>')

def buildings(request, number):
	return HttpResponse('Hey you chose %s.' % number)

def suites(request, number):
	response = 'Shes at least a %s'
	return HttpResponse(response % number)
