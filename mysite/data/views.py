from django.shortcuts import render
from django.views import View
from collections import OrderedDict
from .fusioncharts import FusionCharts

# Create your views here.
def arrest(request) :
    return render(request, 'data/arrest.html')
def location(request) :
    return render(request, 'data/location.html')
def safemap(request) :
    return render(request, 'data/safemap.html')
def region(request) :
    return render(request, 'data/region.html')
    return render(request, 'data/region.html')

