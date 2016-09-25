#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import include, url

from . import views

# 给定命名空间 有此 模板中的detail/results等 可使用 polls:detail/ polls:results
app_name = 'polls'

urlpatterns = [
    # url(r'^$', views.hello, name='hello'),
    url(r'^$', views.index, name='index'),
    # 传参给question_id
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]
