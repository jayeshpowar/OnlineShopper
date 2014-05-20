from django.contrib.auth.models import User
from rest_framework import serializers
from apps.carshop.models import Dealer, Car


class DealerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dealer
        fields = ('id', 'name', 'location', 'brokerage_charge')


class CarsSerializer(serializers.Serializer):
    """
    Section which defines the fields that are to be serialized .
    """
    pk = serializers.Field()
    name = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    dealer = serializers.IntegerField()


    """
    Method to deserialize object
    """
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.name = attrs.get("name", instance.name)
            instance.quantity = attrs.get("quantity", instance.quantity)
            instance.price = attrs.get("price", instance.price)
            instance.dealer = attrs.get("dealer", instance.price)

        return super(CarsSerializer, self).restore_object(attrs, instance)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

