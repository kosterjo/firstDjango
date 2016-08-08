from django.conf.urls import url, include, patterns
from django.contrib import admin

from . import views

app_name = 'leasingPortal'

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^buildings/$', views.buildings, name = 'buildings'),
  url(r'^buildings/(?P<building_id>[0-9]+)/edit/submit$', 
    views.post_building_edit, name = 'post_building_edit'),
  url(r'^buildings/(?P<building_id>[0-9]+)/edit/$', 
      views.building_edit, name = 'building_edit'),
  url(r'^buildings/(?P<building_id>[0-9]+)/add/$', 
      views.post_add_suite, name = 'post_add_suite'),
]
