#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import include, url

from . import views

# 给定命名空间 有此 模板中的detail/results等 可使用 polls:detail/ polls:results
app_name = 'polls'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    # 未引用 as_view() 的url
    # 传参给question_id
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
]
