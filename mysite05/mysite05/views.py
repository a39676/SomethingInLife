#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

import datetime

def hello(request):
    return HttpResponse("Hello world in mysite")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)