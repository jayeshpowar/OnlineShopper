from rest_framework.viewsets import ModelViewSet
from apps.carshop.models import Dealer, Car
from apps.carshop.serializers import DealerSerializer, CarsSerializer


class DealersViewSet(ModelViewSet):
    model = Dealer

    """
    Using the model attribute hence queryset and serializer class are not
    required . The remaining attributes are automatically selected .
    """
    # queryset = AuthorizedDealer.objects.all()
    # serializer_class = DealerSerializer


class CarsViewSet(ModelViewSet):
    model = Car

    # queryset = Car.objects.all()
    # serializer_class = CarsSerializer