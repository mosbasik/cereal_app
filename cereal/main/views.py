from main.models import Manufacturer, Cereal, Kind, Shelf

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {}
    return render(request, 'home.html', context)


def manufacturers(request):
    context = {}
    context['manufacturers'] = Manufacturer.objects.all()
    return render(request, 'manufacturers.html', context)


def mfr_details(request, mfr_id=None):
    context = {}
    manufacturer = Manufacturer.objects.get(id=mfr_id)
    context['manufacturer'] = manufacturer
    context['cereals'] = manufacturer.cereal_set.all()
    return render(request, 'mfr_details.html', context)


def cereals(request):
    context = {}
    context['cereals'] = Cereal.objects.all()
    return render(request, 'cereals.html', context)


def cereal_details(request, cereal_id=None):
    context = {}
    context['cereal'] = Cereal.objects.get(id=cereal_id)
    return render(request, 'cereal_details.html', context)


def kinds(request):
    response = list()
    response.append('<h2><a href="/home">Home<a></h2><br>')
    response.append('<h1><a href="/kinds">Kinds</a></h1><br>')
    kinds = Kind.objects.all()
    for kind in kinds:
        response.append('<a href="%s">%s Cereals</a><br>' % (kind.id,
                                                             kind.name))
    return HttpResponse(response)


def kind_details(request, kind_id=None):
    response = list()
    response.append('<h2><a href="/home">Home<a></h2><br>')
    response.append('<h2><a href="/kinds">Kinds</a></h2><br>')
    kind = Kind.objects.get(id=kind_id)
    response.append('<h1><a href="/kinds/%s">%s Cereals</a></h1><br>' %
                    (kind.id, kind.name))
    for cereal in kind.cereal_set.all():
        response.append('- <a href="/cereals/%s">%s<a><br>' % (cereal.id,
                                                               cereal.name))
    return HttpResponse(response)


def shelves(request):
    response = list()
    response.append('<h2><a href="/home">Home<a></h2><br>')
    response.append('<h1><a href="/shelves">Shelves</a></h1><br>')
    shelves = Shelf.objects.all().order_by('number')
    for shelf in shelves:
        response.append('<a href="%s">Shelf %s</a><br>' % (shelf.id,
                                                           str(shelf.number)))
    return HttpResponse(response)


def shelf_details(request, shelf_id=None):
    response = list()
    response.append('<h2><a href="/home">Home<a></h2><br>')
    response.append('<h2><a href="/shelves">Shelves</a></h2><br>')
    shelf = Shelf.objects.get(id=shelf_id)
    response.append('<h1><a href="/shelves/%s">Shelf %s</a></h1><br>' %
                    (shelf.id, str(shelf.number)))
    for cereal in shelf.cereal_set.all():
        response.append('- <a href="/cereals/%s">%s<a><br>' % (cereal.id,
                                                               cereal.name))
    return HttpResponse(response)


