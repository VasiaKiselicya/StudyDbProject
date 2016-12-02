from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Placement(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=70)
    home_number = models.PositiveIntegerField()


class Departament(models.Model):
    departament_name = models.CharField(max_length=50)
    placement = models.ForeignKey(Placement,
                                  related_name='departament_placement',
                                  on_delete=models.PROTECT)
    status = models.CharField(max_length=20)


class ResponsiblePersons(models.Model):
    full_name = models.CharField(max_length=100)
    residence_street = models.CharField(max_length=50)
    salary = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    premium = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    male = models.CharField(max_length=10)


class FixedAssets(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=15, decimal_places=3)
    inventory_number = models.CharField(max_length=8)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    placement = models.ForeignKey(Placement,
                                  related_name='fixed_assets_placement',
                                  on_delete=models.PROTECT)
    departament = models.ForeignKey(Departament,
                                    related_name='fixed_assets_departament',
                                    on_delete=models.PROTECT)
    persons = models.ForeignKey(ResponsiblePersons,
                                related_name='fixed_assets_persons',
                                on_delete=models.PROTECT)

