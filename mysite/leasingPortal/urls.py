from django.conf.urls import url, include, patterns
from django.contrib import admin

from . import views

app_name = 'leasingPortal'

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^buildings/$', views.buildings, name = 'buildings'),
  url(r'^buildings/add/$', views.add_building, name = 'add_building'),
  url(r'^buildings/add/post$', views.post_add_building, 
  	  name = 'post_add_building'),
  url(r'^buildings/(?P<building_id>[0-9]+)/edit/$', 
      views.building_edit, name = 'building_edit'),
  url(r'^buildings/(?P<building_id>[0-9]+)/edit/submit$', 
    views.post_building_edit, name = 'post_building_edit'),
  url(r'^buildings/(?P<building_id>[0-9]+)/delete/$', 
      views.delete_building, name = 'delete_building'),
  url(r'^buildings/(?P<building_id>[0-9]+)/addSuite/$',  
  	  views.add_suite, name = 'add_suite'),
  url(r'^buildings/(?P<building_id>[0-9]+)/addSuite/post/$', 
      views.post_add_suite, name = 'post_add_suite'),
  url(r'^buildings/(?P<building_id>[0-9]+)/suites/(?P<suite_id>[0-9]+)/$', 
      views.edit_suite, name = 'edit_suite'),
  url(r'^buildings/(?P<building_id>[0-9]+)/suites/(?P<suite_id>[0-9]+)/post$', 
      views.post_edit_suite, name = 'post_edit_suite'),
]
