from .models import Quotes
from django.forms import ModelForm

class QuotesForm(ModelForm):
  class Meta:
    model = Quotes
    fields = ['quotes']