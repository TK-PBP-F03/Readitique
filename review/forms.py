from .models import BookReview
from django.forms import ModelForm

class ReviewForm(ModelForm):
  class Meta:
    model = BookReview
    fields = ['review']