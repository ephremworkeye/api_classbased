from django.urls import path
from .views import AllManufacturer, AllCar

urlpatterns = [
    path('manufacturer', AllManufacturer.as_view(), name='manufacturer'),
    path('car', AllCar.as_view(), name='car'),
]
