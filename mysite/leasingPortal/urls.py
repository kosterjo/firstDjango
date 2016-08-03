from django.conf.urls import url, include, patterns
from django.contrib import admin
#from leasingPortal import views
import views

app_name = 'leasingPortal'

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^buildings/$', views.buildings, name = 'buildings'),
  url(r'^buildings/(?P<building_id>[0-9]+)/$', 
      views.building_detail, name = 'building_detail'),
  url(r'^buildings/(?P<building_id>[0-9]+)/edit/$', 
      views.building_edit, name = 'building_edit'),
  url(r'^buildings/(?P<building_id>[0-9]+)/add/$', 
      views.add_suite, name = 'add_suite'),
]
