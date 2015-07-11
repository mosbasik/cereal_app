from main.models import Manufacturer

from django.shortcuts import render
from django.http import HttpResponse


def manufacturers(request):
    response = ['<h1>Cereal Manufacturers</h1><br>']
    manufacturers = Manufacturer.objects.all()
    for manufacturer in manufacturers:
        response.append('%s<br>' % manufacturer.name)
    return HttpResponse(response)


def details(request, istartswith=None):
    response = ['<h1>Cereal Manufacturers</h1><br>']
    manufacturers = Manufacturer.objects.filter(
        name__istartswith=istartswith)
    for manufacturer in manufacturers:
        response.append('<h2>%s</h2><br>' % manufacturer.name)
        for cereal in manufacturer.cereal_set.all():
            response.append('- %s<br>' % cereal.name)
    return HttpResponse(response)
