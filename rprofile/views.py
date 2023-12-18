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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from rprofile.forms import BookForm
from rprofile.models import UserProfile
from .forms import UpdatePhoneNumberForm
from .forms import BookSearchForm
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile
from api.serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@login_required
def profile(request):
    user = request.user
    user_profile_id = None  # Initialize user_profile_id as None

    try:
        user_profile = UserProfile.objects.get(user=user)
        user_profile_id = user_profile.id  # type: ignore # Retrieve the user_profile_id
    except UserProfile.DoesNotExist:
        user_profile = None

    author_names = Book.objects.values_list('author', flat=True)
    role = "Reader"

    if user.is_superuser:
        role = "Admin"
    elif user.username.replace('+', ' ') in author_names:
        role = "Writer"

    return render(request, 'profile.html', {'user': user, 'user_profile': user_profile, 'role': role, 'user_profile_id': user_profile_id})

def bookofchoice(request):
    # Load JSON data containing a collection of books
    all_books = Book.objects.all()

    if all_books:
        # Randomly select one book from the list
        random_book = random.choice(all_books)
    else:
        random_book = None  # Handle the case where there are no books in the database
    

    return render(request, 'bookofyourchoice.html', {'book': random_book})

def not_login(request):
    return render(request, 'not_login.html')


@login_required
def update_email(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email')
        
        if email:
            user.email = email
            user.save()
            return JsonResponse({'message': 'Email updated successfully'}, status=200)
        
        else:
            return JsonResponse({'error': 'Email data not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
@login_required
def update_phone(request):
    if request.method == 'POST':
        user = request.user
        phone = request.POST.get('phone')
        
        if phone:
            user.profile.phone = phone  # Assuming user has a related 'profile' model
            user.profile.save()
            return JsonResponse({'message': 'Phone updated successfully'}, status=200)
        
        else:
            return JsonResponse({'error': 'Phone data not provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    

    

def edit_book(request, id):
    # Get product berdasarkan ID
    book = Book.objects.get(pk=id)

    # Set product sebagai instance dari form
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_book.html", context)


@api_view(['GET'])
def show_json(request):
    data = UserProfile.objects.all()
    serializer = UserProfileSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_json_by_id(request, id):
    data = UserProfile.objects.filter(pk=id)
    serializer = UserProfileSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_json_by_username(request, username):
    try:
        user_profile = UserProfile.objects.get(user__username=username)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

def update_phone_number(request):
    if request.method == 'POST':
        form = UpdatePhoneNumberForm(request.POST)
        
        if form.is_valid():
            user_profile_id = form.cleaned_data['user_profile_id']
            new_phone_number = form.cleaned_data['new_phone_number']
            
            try:
                user_profile = UserProfile.objects.get(id=user_profile_id)
                user_profile.handphone = new_phone_number
                user_profile.save()
                return JsonResponse({'message': 'Phone number updated successfully'})
            except UserProfile.DoesNotExist:
                return JsonResponse({'error': 'User profile not found'})
        else:
            return JsonResponse({'error': 'Form data is invalid'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    


def filter_books(request):
    if request.method == "POST":
        form = BookSearchForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            author = form.cleaned_data.get('author')
            genre = form.cleaned_data.get('genre')

            # Get the user's profile
            user_profile = UserProfile.objects.get(user=request.user)

            # Filter the user's favorite books based on criteria
            filtered_books = user_profile.favorite_books.filter(
                title__icontains=title,
                author__icontains=author,
                genre__icontains=genre
            )

            return render(request, 'filtered_books.html', {'filtered_books': filtered_books})

    else:
        form = BookSearchForm()

    return render(request, 'filter_books.html', {'form': form})

    
@csrf_exempt
def create_flutter(request, username):  # Change 'user' to 'username' in the method signature
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Retrieve the user
            user = get_object_or_404(User, username=username)

            # Retrieve or create the user profile
            user_profile, created = UserProfile.objects.get_or_create(user=user)

            # Update the user profile
            user_profile.email = data["email"]
            
            # Save the changes
            user_profile.save()

            return JsonResponse({"status": "success"}, status=200)

        except UserProfile.DoesNotExist:
            return JsonResponse({"status": "error", "message": "UserProfile not found"}, status=404)

        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    else:
        return JsonResponse({"status": "error"}, status=401)
    
class UserProfileAPIView(APIView):
    def get(self, request, pk):
        user_profile = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserProfileAPIViewM(APIView):
    def get(self, request, username):  # Change 'pk' to 'username' in the method signature
        user_profile = get_object_or_404(UserProfile, user__username=username)  # Change 'pk' to 'user__username'
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)