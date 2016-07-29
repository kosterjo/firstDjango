from django.conf.urls import url, include, patterns
from django.contrib import admin
from leasingPortal import views

app_name = 'leasingPortal'

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^buildings/$', views.buildings, name = 'buildings'),
  url(r'^buildings/(?P<building_id>[0-9]+)/', 
  views.building_detail, name = 'building_detail')
]
