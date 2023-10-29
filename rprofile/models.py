from django.db import models
from django.contrib.auth.models import User
from main.models import Book

# Create your models here.
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  handphone = models.IntegerField(default=1234567890, null = True, blank = True)
  email = models.TextField(default ="", null = True, blank = True)
  favorite_books = models.ManyToManyField(Book, blank=True)

  #  profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

  def __str__(self):
      return self.user.username

