from django.db import models

# Create your models here.

class Book(models.Model):
    accno=models.CharField(max_length=255)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    Objects=models.Manager() 

