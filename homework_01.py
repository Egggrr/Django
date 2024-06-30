from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    favorite_ice_cream = models.CharField(max_length=100)

class IceCream(models.Model):
    flavor = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.IntegerField()

class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    ice_creams = models.ManyToManyField(IceCream)