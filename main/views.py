from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rprofile.models import UserProfile

# Create your views here.


# Create your views here.

def show_main(request):
    data = Book.objects.order_by("?")[:6]
    user = request.user
    context = {
        'data': data,
        'user': user,
    }

    return render(request, "main.html", context)


def get_filtered(request):
    search_key = request.GET.get('search_text', '')

    if (search_key == ''):
        data = Book.objects.order_by("?")[:6]
    else:
      data = Book.objects.filter(title__icontains=search_key)[:6]

    data_json = serializers.serialize("json", data)

    return HttpResponse(data_json)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # Create a new User instance
            user = form.save()
            
            # # Create a UserProfile and associate it with the User
            user_profile = UserProfile(user=user)
            user_profile.save()

            login(request, user)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:show-main')

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show-main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect("main:show-main")

def book_detail(request,book_id):
    book = get_object_or_404(Book,id=book_id + 1)
    context = {'book':book}

    return render(request, 'book_detail.html', context)

@login_required
def add_to_reading_list(request, book_id):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    book = Book.objects.get(id=book_id+1)
    user_profile.favorite_books.add(book)
    user_profile.save()
    return redirect('bom:show_top_books')  # Ganti 'book_list' dengan URL yang sesuai

