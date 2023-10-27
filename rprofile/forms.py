from django import forms
from main.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','genre', 'rating']

class UpdatePhoneNumberForm(forms.Form):
    new_phone_number = forms.IntegerField()