# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200)
    code = models.CharField(blank=True, null=True, max_length=10)
    population = models.IntegerField(blank=True, null=True)
    total_notices = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'country'


class Nationality(models.Model):
    nationality = models.ForeignKey(Country, models.DO_NOTHING)
    notice = models.ForeignKey('Notice', models.DO_NOTHING)

    class Meta:
        db_table = 'nationality'


class Notice(models.Model):
    entity_id = models.CharField(blank=True, null=True, max_length=200)
    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(blank=True, null=True, max_length=10)
    place_of_birth = models.CharField(blank=True, null=True, max_length=200)
    charge = models.TextField(blank=True, null=True, max_length=1000)
    country = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        db_table = 'notice'
