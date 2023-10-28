from django.shortcuts import render
from addbuku.models import NewBook
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def add_buku(request):
    user = request.user
    if user.is_authenticated:
        newbooks = NewBook.objects.all()
    else:
        newbooks = NewBook.objects.all()[:6]
    context = {
        'newbooks': newbooks,
        'user': user,
    }

    return render(request,'addbuku.html',context)

def get_newbook_json(request):
    user = request.user
    if user.is_authenticated:
        new_book_item = NewBook.objects.all()
    else:
        new_book_item = NewBook.objects.all()[:6]
    return HttpResponse(serializers.serialize('json', new_book_item))

@csrf_exempt
def add_newbook_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        genre = request.POST.get("genre")
        image_link = request.POST.get("image_link")

        new_book = NewBook(title=title,author=author,description=description,genre=genre,image_link=image_link)
        new_book.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()