from rest_framework import serializers
from apps.carshop.models import Dealer, Car


class DealerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dealer
        fields = ('id', 'name', 'location', 'brokerage_rate')


class CarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'quantity', 'price')
