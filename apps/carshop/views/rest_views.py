from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.carshop.models import Dealer, Car
from apps.carshop.serializers import UserSerializer, DealerSerializer, \
    CarsSerializer
from rest_framework import permissions


"""
api_view enables the presence of request and response object . The format is used
for specifying json or any other format
"""


@api_view(['GET', 'POST'])
def get_user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarlistView(APIView):
    def get(self, request, format=None):
        cars = Car.objects.all()
        serializer = UserSerializer(cars, many=True)
        return Response(serializer)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DealerListView(ListAPIView):

        queryset = Dealer.objects.all()
        serializer_class = DealerSerializer

class DealerListCreateView(ListCreateAPIView):
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        queryset = Dealer.objects.all()
        serializer_class = DealerSerializer

class DealerListDetailView(RetrieveUpdateDestroyAPIView):
        queryset = Dealer.objects.all()
        serializer_class = DealerSerializer

class CarListDetailView(RetrieveUpdateDestroyAPIView):
        queryset = Car.objects.all()
        serializer_class = CarsSerializer



# class DealersViewSet(ModelViewSet):
#     model = Dealer
#
#     """
#     Using the model attribute hence queryset and serializer class are not
#     required . The remaining attributes are automatically selected .
#     """
#
#
#     # queryset = AuthorizedDealer.objects.all()
#     # serializer_class = DealerSerializer
#
#
# class CarsViewSet(ModelViewSet):
#     model = Car
    # queryset = Car.objects.all()
    # serializer_class = CarsSerializer