from django.db import models

# Create your models here.

class Book(models.Model):
    idno=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    mark1=models.IntegerField()
    mark2=models.IntegerField()
    mark3=models.IntegerField()

    Objects=models.Manager() 

