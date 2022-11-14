from django.contrib import admin
from .models import Area, Country, District, Locality, AreaPoint, Location
# from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin


class AreaAdmin(LeafletGeoAdmin):
    list_display = ('name', 'id')


class CountryAdmin(LeafletGeoAdmin):
    list_display = ('name', 'cuatm')


class DistrictAdmin(LeafletGeoAdmin):
    list_display = ('name', 'type')


class LocalityAdmin(LeafletGeoAdmin):
    list_display = ('name', 'population')


class AreaPointAdmin(LeafletGeoAdmin):
    list_display = ('denumirea', 'categorie')


class LocationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


admin.site.register(Area, AreaAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(AreaPoint, AreaPointAdmin)
admin.site.register(Location, LocationAdmin)
