from django.urls import path
from .views import MapPageView, country_dataset,  area_dataset, \
    district_dataset, locality_dataset, area_point_dataset, location_dataset

app_name = 'map'

urlpatterns = [
    path('', MapPageView.as_view(), name='map'),
    path('area_data/', area_dataset, name='area'),
    path('country_data/', country_dataset, name='country'),
    path('district_data/', district_dataset, name='district'),
    path('locality_data/', locality_dataset, name='locality'),
    path('area_point_data/', area_point_dataset, name='area_point'),
    path('location_data/', location_dataset, name='location'),
]