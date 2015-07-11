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


class CerealInline(admin.TabularInline):
    model = Cereal


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', )
    inlines = [CerealInline]


class KindAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', )
    inlines = [CerealInline]


class ShelfAdmin(admin.ModelAdmin):
    list_display = ('number', )
    inlines = [CerealInline]


admin.site.register(Cereal, CerealAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Kind, KindAdmin)
admin.site.register(Shelf, ShelfAdmin)
