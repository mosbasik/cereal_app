#!/usr/bin/env python

import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cereal.settings")

from main.models import Cereal, Manufacturer, Kind, Shelf

cereal_csv = os.path.join(os.path.dirname(os.path.abspath('__file__')),
                          'cereal.csv')

with open(cereal_csv, 'r') as cereal_file:
    # create a DictReader iterator from the csv file
    reader = csv.DictReader(cereal_file, delimiter=';')

    # skip the first line of data (it's not really data)
    reader.next()

    # Cereal.objects.all().delete()

    for row in reader:

        # get or create manufacturer
        new_manufacturer, created = Manufacturer.objects.get_or_create(
                abbreviation=row['mfr'])
        new_manufacturer.save()

        # get or create kind
        new_kind, created = Kind.objects.get_or_create(
                abbreviation=row['type'])
        new_kind.save()

        # get or create shelf
        new_shelf, created = Shelf.objects.get_or_create(
                number=row['shelf'])
        new_shelf.save()

        # get or create cereal
        new_cereal, created = Cereal.objects.get_or_create(
                name=row['name'])
        new_cereal.manufacturer = new_manufacturer
        new_cereal.kind = new_kind
        new_cereal.calorie = row['calories']
        new_cereal.protein = row['protein']
        new_cereal.fat = row['fat']
        new_cereal.sodium = row['sodium']
        new_cereal.fiber = row['fiber']
        new_cereal.carb = row['carbo']
        new_cereal.sugar = row['sugars']
        new_cereal.potassium = row['potass']
        new_cereal.vitamin = row['vitamins']
        new_cereal.shelf = new_shelf
        new_cereal.weight = row['weight']
        new_cereal.cup = row['cups']
        new_cereal.rating = row['rating']
        new_cereal.save()
