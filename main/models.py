from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/')
    upload_at = models.DateTimeField(auto_now_add=True)

    power = models.FloatField()
    material = models.CharField(max_length=50)
    pressure_min = models.FloatField()
    pressure_max = models.FloatField()
    autofire = models.BooleanField()
    weight = models.FloatField()
    size_x = models.IntegerField()
    size_y = models.IntegerField()
    size_z = models.IntegerField()
    flame_control = models.BooleanField()
    fuel_type = models.CharField(max_length=50)