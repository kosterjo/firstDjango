from django.shortcuts import render, get_object_or_404
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
	building = get_object_or_404(Building, pk=building_id) 
	return render(request, 'buildings/detail.html', {'building': building} )
