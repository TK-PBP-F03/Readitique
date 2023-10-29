from django.db import models
from main.models import Book
from django.contrib.auth.models import User

# Create your models here.

class BookReview(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  review = models.TextField()

  def __str__(self):
    return f"{self.user.username} - {self.book.title}"