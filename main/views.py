from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import BookForm
from django.urls import reverse
from .models import Book
import json
import codecs
from django.http import HttpResponse
from django.core import serializers
# Create your views here.


def show_main(request):
    data = Book.objects.all()
    context = {
        'name': 'Rapunz',
        'class': 'PBP F',
        'data': data,
    }

    return render(request, "main.html", context)


def create_books_from_json(data):
    books = []
    for entry in data:
        book = Book(
            title=entry['Book'],
            author=entry['Author'],
            description=entry['Description'],
            genre=entry['Genres']
        )
        books.append(book)
    return books


def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_book.html", context)


def show_xml(request):
    data = get_data()
    books = create_books_from_json(data)
    serialized_data = serializers.serialize("xml", books)
    return HttpResponse(serialized_data, content_type="application/xml")


def show_json(request):
    data = get_data()
    books = create_books_from_json(data)
    serialized_data = serializers.serialize("json", books)
    return HttpResponse(serialized_data, content_type="application/json")
