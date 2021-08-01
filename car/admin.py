from django.contrib import admin
from .models import Manufacturer, Car

# Register your models here.
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'name', 'slug', 'car_model', 'car_year']
    prepopulated_fields = {'slug':('slug',)}