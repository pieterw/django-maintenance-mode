# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from maintenance_mode.views import maintenance_mode_off, maintenance_mode_on


urlpatterns = patterns('',
    url(r'^off/$', maintenance_mode_off, name='maintenance_mode_off'), 
    url(r'^on/$', maintenance_mode_on, name='maintenance_mode_on'), 
)

