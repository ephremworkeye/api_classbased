from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
  


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_year = models.IntegerField()

    def __str__(self):
        return self.name
    


