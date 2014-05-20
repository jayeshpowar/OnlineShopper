from django.db import models

# Create your models here.
from django.db.models import Model


class Dealer(Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    brokerage_charge = models.IntegerField()


class Car(Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.DateField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    dealer = models.ForeignKey(Dealer)


    def __unicode__(self):
        return self.name




