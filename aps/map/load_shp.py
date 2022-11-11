import os
from django.contrib.gis.utils import LayerMapping
from .models import Arie, Tara, Rn, Localitate, AriePoint


# Auto-generated `LayerMapping` dictionary for Arii model
arie_mapping = {
    'gid': 'gid',
    'id': 'id',
    'categoria': 'categoria',
    'name': 'name',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for Moldova model
tara_mapping = {
    'name': 'name',
    'cuatm': 'cuatm',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for Raioane model
raion_mapping = {
    'name': 'name',
    'type': 'type',
    'engtype': 'engtype',
    'gid': 'gid',
    'hasc': 'hasc',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for Localitati model
localitate_mapping = {
    'id': 'id',
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'population': 'population',
    'name': 'name',
    'geom': 'MULTIPOINT',
}

ariepoint_mapping = {
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

arie_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/geo_ap_pol_4326.shp'))
tara_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/geo_mda_adm0_pol_4326.shp'))
raion_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/geo_mda_adm1_pol_4326.shp'))
localitate_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/geo_mda_adm2_point_4326.shp'))
ariepoint_shp = os.path .abspath(os.path.join(os.path.dirname(__file__), 'data/ap_4326.shp'))


def run_ariepoint(verbose=True):
    lm = LayerMapping(AriePoint, ariepoint_shp, ariepoint_mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_arie(verbose=True):
    lm = LayerMapping(Arie, arie_shp, arie_mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_tara(verbose=True):
    lm = LayerMapping(Tara, tara_shp, tara_mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_raion(verbose=True):
    lm = LayerMapping(Rn, raion_shp, raion_mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)


def run_localitate(verbose=True):
    lm = LayerMapping(Localitate, localitate_shp, localitate_mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
