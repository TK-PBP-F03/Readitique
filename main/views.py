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
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:show-main')
    context = {'form':form}
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

