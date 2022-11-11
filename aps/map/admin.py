from django.contrib import admin
from .models import Arie, Tara, Rn, Localitate, AriePoint, Locatie
# from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin


class ArieAdmin(LeafletGeoAdmin):
    list_display = ('name', 'id')


class TaraAdmin(LeafletGeoAdmin):
    list_display = ('name', 'cuatm')


class RnAdmin(LeafletGeoAdmin):
    list_display = ('name', 'type')


class LocalitateAdmin(LeafletGeoAdmin):
    list_display = ('name', 'population')


class AriePointAdmin(LeafletGeoAdmin):
    list_display = ('denumirea', 'categorie')


class LocatieAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


admin.site.register(Arie, ArieAdmin)
admin.site.register(Tara, TaraAdmin)
admin.site.register(Rn, RnAdmin)
admin.site.register(Localitate, LocalitateAdmin)
admin.site.register(AriePoint, AriePointAdmin)
admin.site.register(Locatie, LocatieAdmin)
