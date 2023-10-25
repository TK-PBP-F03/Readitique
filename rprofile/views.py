import json
import random
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Book
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    user = request.user
    author_names = Book.objects.values_list('author', flat=True)  # Get a list of all author names from the database
    role = "Reader"  # Default role is "Reader"

    if user.is_superuser:
        role = "Admin"
    elif user.username in author_names:
        role = "Writer"

    return render(request, 'profile.html', {'user': user, 'role': role})

def bookofchoice(request):
    # Load JSON data containing a collection of books
    all_books = Book.objects.all()

    if all_books:
        # Randomly select one book from the list
        random_book = random.choice(all_books)
    else:
        random_book = None  # Handle the case where there are no books in the database
    

    return render(request, 'bookofyourchoice.html', {'book': random_book})
