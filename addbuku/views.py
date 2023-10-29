from django.shortcuts import render
from addbuku.models import Book, NewBook, UserVote
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

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

    return render(request,'addbuku.html', context)

def get_filtered(request):
    user = request.user
    search_key = request.GET.get('search_text', '')
    
    if user.is_authenticated:
        if (search_key == ''):
            data = NewBook.objects.order_by("-votes")
        else:
            data = NewBook.objects.filter(title__icontains=search_key).order_by("-votes")
    else:
        if (search_key == ''):
            data = NewBook.objects.order_by("-pk")[:6]
        else:
            data = NewBook.objects.filter(title__icontains=search_key).order_by("-pk")[:6]

    data_json = serializers.serialize("json", data)

    return HttpResponse(data_json)

def get_newbook_json(request):
    user = request.user
    if user.is_authenticated:
        new_book_item = NewBook.objects.all().order_by('-votes')
    else:
        new_book_item = NewBook.objects.all().order_by('-pk')[:6]
    return HttpResponse(serializers.serialize('json', new_book_item))

@csrf_exempt
def add_newbook_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        author = request.POST.get("author")
        description = request.POST.get("description")
        genre = request.POST.get("genre")
        image_link = request.POST.get("image_link")
        user = request.user

        new_book = NewBook(title=title,author=author,description=description,genre=genre,image_link=image_link)
        new_book.save()
        UserVote.objects.create(user=user, book=new_book)

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def increment_votes(request, id):
    if request.method == 'POST':
        new_book = NewBook.objects.get(pk=id)
        user = request.user
        print(new_book.votes)
        if UserVote.objects.filter(user=user, book=new_book).exists():
            return JsonResponse({'error': 'You have already voted for this book.'}, status=400)

        new_book.votes += 1
        print(new_book.votes)
        new_book.save()
        UserVote.objects.create(user=user, book=new_book)
        return HttpResponse(b"OK", status=200)

    return HttpResponseNotFound()

@csrf_exempt
def approve_book(request, id):
    if request.method == 'GET':
        new_book = NewBook.objects.get(pk=id)
        last_book = Book.objects.last()
        title = new_book.title
        author = new_book.author
        description = new_book.description
        genre = new_book.genre
        image_link = new_book.image_link
        default_user = User.objects.get(username="bwahaj")
        
        book = Book(
            index_key=last_book.index_key+1, 
            title=title, 
            author=author, 
            description=description, 
            genre=genre, 
            rating=0, 
            image_link=image_link,
            count_read = 0,
            user = default_user,
            )
        book.save()

        new_book.delete()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()
