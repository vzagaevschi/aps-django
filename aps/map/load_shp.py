import os
from django.contrib.gis.utils import LayerMapping
from .models import Area, AreaPoint, Country, District, Locality, Location

area_mapping = {
    'gid': 'gid',
    'id': 'id',
    'categoria': 'categoria',
    'name': 'name',
    'geom': 'MULTIPOLYGON',
}

country_mapping = {
    'name': 'name',
    'cuatm': 'cuatm',
    'geom': 'MULTIPOLYGON',
}

district_mapping = {
    'name': 'name',
    'type': 'type',
    'engtype': 'engtype',
    'gid': 'gid',
    'hasc': 'hasc',
    'geom': 'MULTIPOLYGON',
}

locality_mapping = {
    'id': 'id',
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'population': 'population',
    'name': 'name',
    'geom': 'MULTIPOINT',
}

area_point_mapping = {
    'objectid': 'OBJECTID',
    'id': 'ID',
    'denumirea': 'DENUMIREA',
    'suprafata': 'SUPRAFATA',
    'infiintari': 'INFIINTARI',
    'categorie': 'CATEGORIE',
    'mn_id': 'MN_ID',
    'pa_code': 'PA_CODE',
    'geom': 'MULTIPOINT',
}

area_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        'data/geo_ap_pol_4326.shp'))
country_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           'data/geo_mda_adm0_pol_4326.shp'))
district_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            'data/geo_mda_adm1_pol_4326.shp'))
locality_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            'data/geo_mda_adm2_point_4326.shp'))
area_point_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                              'data/ap_4326.shp'))


def run_area_point(verbose=True):
    lm = LayerMapping(AreaPoint, area_point_shp, area_point_mapping,
                      transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_area(verbose=True):
    lm = LayerMapping(Area, area_shp, area_mapping, transform=False,
                      encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_country(verbose=True):
    lm = LayerMapping(Country, country_shp, country_mapping, transform=False,
                      encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_district(verbose=True):
    lm = LayerMapping(District, district_shp, district_mapping,
                      transform=False,
                      encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_locality(verbose=True):
    lm = LayerMapping(Locality, locality_shp, locality_mapping,
                      transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
