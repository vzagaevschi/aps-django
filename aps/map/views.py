from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Arie, Tara, Rn, Localitate, AriePoint, Locatie


class MapPageView(TemplateView):
    template_name = 'map.html'


def arie_dataset(request):
    arie = serialize('geojson', Arie.objects.all())
    return HttpResponse(arie, content_type='json')


def tara_dataset(request):
    tara = serialize('geojson', Tara.objects.all())
    return HttpResponse(tara, content_type='json')


def raion_dataset(request):
    raion = serialize('geojson', Rn.objects.all())
    return HttpResponse(raion, content_type='json')


def localitate_dataset(request):
    localitate = serialize('geojson', Localitate.objects.all())
    return HttpResponse(localitate, content_type='json')


def ariepoint_dataset(request):
    ariepoint = serialize('geojson', AriePoint.objects.all())
    return HttpResponse(ariepoint, content_type='json')


def locatie_dataset(request):
    locatie = serialize('geojson', Locatie.objects.all())
    return HttpResponse(locatie, content_type='json')
