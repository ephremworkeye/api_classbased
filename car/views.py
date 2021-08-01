# from django.shortcuts import render
from .serializers import ManufacturerSerializer, CarSerializer
from .models import Manufacturer, Car
from rest_framework.generics import ListCreateAPIView
# Create your views here.

class AllManufacturer(ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class AllCar(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer