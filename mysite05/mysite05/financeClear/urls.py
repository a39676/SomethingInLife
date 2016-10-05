#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import include, url

from . import views

app_name = 'financeClear'

urlpatterns = [

    url(r'^hello/$', views.hello, name='hello'),
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]
