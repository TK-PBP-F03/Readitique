import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from main.models import Book
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

import review
from .forms import ReviewForm
from .models import BookReview
from django.contrib.auth.models import User
from django.core import serializers

# Create your views here.

def show_reviews(request):
  book = Book.objects.order_by("?")[:6]

  context = {'data': book}

  return render(request, "reviews.html", context)

def book_review(request, pk):
  try:
    book = get_object_or_404(Book, pk=pk)
    reviews = book.bookreview_set.all()
    print(reviews)
    print("thaariq")
    form = ReviewForm()

    context = {
      'book': book,
      'reviews': reviews,
      'form': form,
    }

    return render(request, "review.html", context)
  
  except Http404:
    return redirect("review:reviews")
  
def get_review_ajax(self, pk):
  book = Book.objects.get(pk=pk)
  reviews = book.bookreview_set.all()

  reviews_json = serializers.serialize('json', reviews)

  print(reviews_json)
  print()

  return JsonResponse(reviews_json, safe=False)
  
@login_required(login_url="main:login")
@csrf_exempt
def create_review(request, pk):
  book = Book.objects.get(pk=pk)
  user = User.objects.get(username=request.user.username)

  print(request.user.username, book)
  
  if request.method == 'POST':
        
      review = ReviewForm(request.POST)

      if review.is_valid():

        old_review = book.bookreview_set.filter(user__username=user.username)
        
        if len(old_review) > 0:
          old_review.delete()

        new_review = review.save(commit=False)

        new_review.user = user
        new_review.book = book

        new_review.save()

        return HttpResponse(b"CREATED", status=201)

  return HttpResponseNotFound


def reviews_JSON(request):
  data = BookReview.objects.all()

  return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def book_reviews_JSON(request, ik):
  ik += 1
  book = Book.objects.get(pk=ik)
  print(book.title)

  data = BookReview.objects.filter(book=book)

  return HttpResponse(serializers.serialize("json", data), content_type="application/json") 

@csrf_exempt
def write_review_flutter(request, ik):
  if (request.method == 'POST'):
    data = json.loads(request.body)
    ik += 1
    book = Book.objects.get(pk=ik)


    old_review = book.bookreview_set.filter(user__username=request.user.username)
        
    if len(old_review) > 0:
      old_review.delete()

    new_review = BookReview.objects.create(
      user = request.user,
      book = book,
      review = data["review"],
    )

    new_review.save()

    return JsonResponse({"status": "success"}, status=200)
  
  else:
      return JsonResponse({"status": "error"}, status=401)