from django.urls import path
from .views import MapPageView, tara_dataset, arie_dataset, raion_dataset, localitate_dataset, ariepoint_dataset, locatie_dataset

app_name = 'map'

urlpatterns = [
    path('', MapPageView.as_view(), name='map'),
    path('arie_data/', arie_dataset, name='arie'),
    path('tara_data/', tara_dataset, name='tara'),
    path('raion_data/', raion_dataset, name='raion'),
    path('localitate_data/', localitate_dataset, name='localitate'),
    path('ariepoint_data/', ariepoint_dataset, name='ariepoint'),
    path('locatie_data/', locatie_dataset, name='locatie'),
]