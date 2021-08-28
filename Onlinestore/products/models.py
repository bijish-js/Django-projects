from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2550) 
    Objects=models.Manager() 

class Offers(models.Model):
    offrname=models.CharField(max_length=255)
    offramt=models.FloatField()
     