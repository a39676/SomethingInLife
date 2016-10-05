#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Accounts(models.Model):
    owner = models.CharField(max_length = 50)
    bankName = models.CharField(max_length = 50)
    cardNumber = models.CharField(max_length = 50)
    cardType = models.CharField(max_length = 50, default = "D")

    def __str__(self):
    	return self.owner, self.bankName


class Cards(models.Model):
    account = models.ForeignKey(Accounts)
    PeriodOfValidity = models.DateTimeField()
    balance = models.IntegerField(default = 0)
    modifyDate = models.DateTimeField(default = timezone.now)

    def __str__(self):
    	return self.balance

