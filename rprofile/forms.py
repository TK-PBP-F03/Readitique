from django import forms
from main.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','genre', 'rating']

class UpdatePhoneNumberForm(forms.Form):
    user_profile_id = forms.IntegerField(widget=forms.HiddenInput())  # A hidden field to store the user_profile_id
    new_phone_number = forms.IntegerField()  # IntegerField for the new phone number

class BookSearchForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)
    genre = forms.CharField(required=False)