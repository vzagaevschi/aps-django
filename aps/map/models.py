from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


# This is an auto-generated Django model module created by ogrinspect.

class Arie(models.Model):
    gid = models.BigIntegerField()
    id = models.CharField(max_length=3, primary_key=True)
    categoria = models.CharField(max_length=100)
    name = models.CharField(max_length=133)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Arii Protejate'


class Tara(models.Model):
    name = models.CharField(max_length=254)
    cuatm = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural = 'Țări'


class Rn(models.Model):
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=50)
    engtype = models.CharField(max_length=50)
    gid = models.CharField(max_length=10)
    hasc = models.CharField(max_length=10)
    geom = models.MultiPolygonField(srid=4326)


    class Meta:
        verbose_name_plural = 'Raioane'


class Localitate(models.Model):
    id = models.BigIntegerField(primary_key=True)
    osm_id = models.CharField(max_length=10)
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28)
    population = models.FloatField()
    name = models.CharField(max_length=100)
    geom = models.MultiPointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Localități'


class Locatie(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Locații'


class AriePoint(models.Model):
    objectid = models.BigIntegerField()
    id = models.FloatField(primary_key=True)
    denumirea = models.CharField(max_length=254)
    suprafata = models.FloatField()
    infiintari = models.FloatField()
    categorie = models.FloatField()
    mn_id = models.FloatField()
    pa_code = models.FloatField()
    geom = models.MultiPointField(srid=4326)

    # def __unicode__(self):
    #     return self.AriePoint

    class Meta:
        verbose_name_plural = 'Arii Protejate (puncte)'

