# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def page1(request, *args, **kwargs):
    return render(request, "page1.html", {})

def page2(request, *args, **kwargs):
    return render(request, "page2.html", {})

def page3(request, *args, **kwargs):
    return render(request, "page2.html", {})

def page4(request, *args, **kwargs):
    return render(request, "page4.html", {})

def page5(request, *args, **kwargs):
    return render(request, "page5.html", {})

def page6(request, *args, **kwargs):
    return render(request, "page6.html", {})
