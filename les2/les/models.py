from django.db import models
from .abstract_models import *


class ValidityPeriod(models.Model):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)


class FormOfTheCabin(models.Model):
    form_of_the_cabin = models.TextField(null=True)


class TypeOfCabin(models.Model):
    type_of_cabin = models.TextField(null=True)


class TreeSpecies(models.Model):
    tree_species = models.CharField(null=True)


class TreeSpecies(models.Model):
    tree_species = models.CharField(null=True)


class Organization(models.Model):
    title = models.CharField(max_length=255, null=True)
    validity_period = models.ForeignKey('ValidityPeriod', on_delete=models.CASCADE, null=True)


class DetailsOfTheOrganization(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True)
    inn = models.IntegerField(null=True)
    kpp = models.IntegerField(null=True)
    ogrn = models.IntegerField(null=True)
    okpo = models.IntegerField(null=True)
    email = models.CharField(max_length=255, null=True)
    validity_period = models.ForeignKey('ValidityPeriod', on_delete=models.CASCADE, null=True)


class BankDetail(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True)
    bank_title = models.TextField(null=True)
    payment_account = models.IntegerField(null=True)
    corset = models.IntegerField(null=True)
    bik = models.IntegerField(null=True)
    validity_period = models.ForeignKey('ValidityPeriod', on_delete=models.CASCADE, null=True)


class Forestry(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True)
    validity_period = models.ForeignKey('ValidityPeriod', on_delete=models.CASCADE, null=True)


class DepartmentAddress(Address, models.Model):
    forestry = models.ForeignKey('Forestry', on_delete=models.CASCADE, null=True)
