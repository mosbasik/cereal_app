from main.models import Manufacturer

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    response = []
    response.append('<h1><a href="/home">Home<a></h1><br>')
    response.append('<a href="/manufacturers">Manufacturers<a><br>')
    return HttpResponse(response)


def manufacturers(request):
    response = list()
    response.append('<h2><a href="/home">Home<a></h2><br>')
    response.append('<h1><a href="/manufacturers">Manufacturers<a></h1><br>')
    manufacturers = Manufacturer.objects.all()
    for manufacturer in manufacturers:
        response.append('<a href="%s">%s</a><br>' % (manufacturer.id,
                                                     manufacturer.name))
    return HttpResponse(response)


def mfr_details(request, mfr_id=None):
    response = list()
    response.append('<h2><a href="/home">Home<a></h2><br>')
    response.append('<h2><a href="/manufacturers">Manufacturers<a></h2><br>')
    manufacturer = Manufacturer.objects.get(id=mfr_id)
    response.append('<h1><a href="/manufacturers/%s">%s</a></h1><br>' %
                    (manufacturer.id, manufacturer.name))
    for cereal in manufacturer.cereal_set.all():
        response.append('- %s<br>' % cereal.name)
    return HttpResponse(response)
