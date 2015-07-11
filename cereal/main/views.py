from main.models import Manufacturer

from django.shortcuts import render
from django.http import HttpResponse


def manufacturers(request):

    manufacturers = Manufacturer.objects.all()
    response = ['<h1>Cereal Manufacturers:</h1><br>']

    for manufacturer in manufacturers:
        response.append('%s<br>' % manufacturer.name)

    return HttpResponse(response)
