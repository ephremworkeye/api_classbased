from rest_framework import serializers
from .models import Manufacturer, Car

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['manufacturer', 'name', 'slug', 'car_model', 'car_year']