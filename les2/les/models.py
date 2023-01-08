from django.db import models


class ValidityPeriod(models.Model):
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)


class Organization(models.Model):
    title = models.CharField(max_length=255)
    validity_period = models.ForeignKey('ValidityPeriod', on_delete=models.CASCADE, null=True)