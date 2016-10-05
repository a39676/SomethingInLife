#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db.models import F
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Accounts, Cards

def hello(request):
    return HttpResponse("Hello world in financeClear")