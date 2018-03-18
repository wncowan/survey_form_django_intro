# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, "survey/index.html")

def process(request):
    if request.method == "POST":
        print('entered process')
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        print(request.session['name'])
        print(request.session['location'])
        print(request.session['language'])
        print(request.session['comments'])
    return redirect('/result')

def result(request):
    request.session['count'] += 1
    context = {
        'my_name' : request.session['name'],
        'my_location' : request.session['location'],
        'my_language' : request.session['language'],
        'my_comments' : request.session['comments'],
        'my_count' : request.session['count']
    }
    return render(request, "survey/result.html", context)
