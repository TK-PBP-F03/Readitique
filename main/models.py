from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=255)