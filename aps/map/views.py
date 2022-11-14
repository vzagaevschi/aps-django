from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Area, Country, District, Locality, Location, AreaPoint


class MapPageView(TemplateView):
    template_name = 'map.html'


def area_dataset(request):
    area = serialize('geojson', Area.objects.all())
    return HttpResponse(area, content_type='json')


def country_dataset(request):
    country = serialize('geojson', Country.objects.all())
    return HttpResponse(country, content_type='json')


def district_dataset(request):
    district = serialize('geojson', District.objects.all())
    return HttpResponse(district, content_type='json')


def locality_dataset(request):
    locality = serialize('geojson', Locality.objects.all())
    return HttpResponse(locality, content_type='json')


def area_point_dataset(request):
    area_point = serialize('geojson', AreaPoint.objects.all())
    return HttpResponse(area_point, content_type='json')


def location_dataset(request):
    location = serialize('geojson', Location.objects.all())
    return HttpResponse(location, content_type='json')
