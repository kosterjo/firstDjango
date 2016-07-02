from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<p>Index view</p>')

def buildings(request):
	return HttpResponse('<p>Buildings view</p>')

def suites(request):
	return HttpResponse('<p>Index view</p>')
