# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response, render


# Create your views here.
def home(request):
    return render(request, 'main/home.html')


def google(request):
    return render_to_response('main/google3d8b31bd23ec2d59.html')


def robots(request):
    return render_to_response('main/Robots.txt')


def sitemap(request):
    return render_to_response('main/sitemap.xml')
