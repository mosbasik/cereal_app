from django.contrib import admin
from main.models import Cereal, Manufacturer, Kind, Shelf


class CerealAdmin(admin.ModelAdmin):
    list_display = ('name',
                    # 'manufacturer',
                    # 'kind',
                    'calorie',
                    'protein',
                    'fat',
                    'sodium',
                    'fiber',
                    'carb',
                    'sugar',
                    'potassium',
                    'vitamin',
                    # 'shelf',
                    'weight',
                    'cup',
                    'rating',)

    # name = models.CharField(max_length=100, null=True, blank=True)
    # manufacturer = models.ForeignKey('main.Manufacturer')
    # kind = models.ForeignKey('main.Kind')
    # calorie = models.IntegerField(null=True, blank=True)
    # protein = models.IntegerField(null=True, blank=True)
    # fat = models.IntegerField(null=True, blank=True)
    # sodium = models.IntegerField(null=True, blank=True)
    # fiber = models.FloatField(null=True, blank=True)
    # carb = models.FloatField(null=True, blank=True)
    # sugar = models.IntegerField(null=True, blank=True)
    # potassium = models.IntegerField(null=True, blank=True)
    # vitamin = models.IntegerField(null=True, blank=True)
    # shelf = models.ForeignKey('main.Shelf')
    # weight = models.FloatField(null=True, blank=True)
    # cup = models.FloatField(null=True, blank=True)
    # rating = models.FloatField(null=True, blank=True)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', )


class KindAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', )


class ShelfAdmin(admin.ModelAdmin):
    list_display = ('number', )


admin.site.register(Cereal, CerealAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Kind, KindAdmin)
admin.site.register(Shelf, ShelfAdmin)