from django.db import models

# Create your models here.
# name;     mfr;            type;           calories;   protein;    fat;    sodium; fiber;  carbo;  sugars; potass; vitamins;   shelf;  weight; cups;   rating
# String;   Categorical;    Categorical;    Int;        Int;        Int;    Int;    Float;  Float;  Int;    Int;    Int;        Int;    Float;  Float;  Float


class Cereal(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.ForeignKey('main.Manufacturer')
    kind = models.ForeignKey('main.Kind')
    calorie = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    fat = models.IntegerField(null=True, blank=True)
    sodium = models.IntegerField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    carb = models.FloatField(null=True, blank=True)
    sugar = models.IntegerField(null=True, blank=True)
    potassium = models.IntegerField(null=True, blank=True)
    vitamin = models.IntegerField(null=True, blank=True)
    shelf = models.ForeignKey('main.Shelf')
    weight = models.FloatField(null=True, blank=True)
    cup = models.FloatField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    abbreviation = models.CharField(max_length=1, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Kind(models.Model):
    abbreviation = models.CharField(max_length=1, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Shelf(models.Model):
    number = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.number
