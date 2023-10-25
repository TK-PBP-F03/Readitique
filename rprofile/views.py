import json
import random
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book
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
    with open('dataset_with_images.json', 'r') as json_file:
        book_data = json.load(json_file)

    # Randomly select one book from the list
    random_book = random.choice(book_data)

    return render(request, 'profile.html', {'book': random_book})
