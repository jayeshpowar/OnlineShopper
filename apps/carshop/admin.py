from django.contrib import admin

# Register your models here.

from apps.carshop.models import Car, Dealer

admin.site.register(Dealer)
admin.site.register(Car)