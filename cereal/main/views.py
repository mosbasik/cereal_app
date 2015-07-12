from main.models import Manufacturer

from django.shortcuts import render
from django.http import HttpResponse


def manufacturers(request):
    response = ['<h1><a href="/manufacturers">Cereal Manufacturers<a></h1><br>']
    manufacturers = Manufacturer.objects.all()
    for manufacturer in manufacturers:
        response.append('<a href="%s">%s</a><br>' % (manufacturer.id,
                                                     manufacturer.name))
    return HttpResponse(response)


def mfr_details(request, mfr_id=None):
    response = ['<h1><a href="/manufacturers">Cereal Manufacturers<a></h1><br>']
    manufacturer = Manufacturer.objects.get(id=mfr_id)
    response.append('<h2>%s</h2><br>' % manufacturer.name)
    for cereal in manufacturer.cereal_set.all():
        response.append('- %s<br>' % cereal.name)
    return HttpResponse(response)
