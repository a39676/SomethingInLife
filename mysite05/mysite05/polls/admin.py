#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib import admin

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)