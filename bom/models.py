from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quotes = models.TextField()
    
    def __str__(self):  
        return f"{self.user.username}"