from django.shortcuts import render
from .models import NewBook
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def add_buku(request):
    user = request.user
    if user.is_authenticated:
        newbooks = NewBook.objects.all
    else:
        newbooks = NewBook.objects.all[:6]
    context = {
        'newbooks': newbooks,
        'user': user,
    }

    return render(request,'addbuku.html',context)

def get_filtered(request):
    search_key = request.GET.get('search_text', '')

    if (search_key == ''):
        data = NewBook.objects.order_by("?")[:6]
    else:
      data = NewBook.objects.filter(title__icontains=search_key)[:6]

    data_json = serializers.serialize("json", data)

    return HttpResponse(data_json)

def get_newbook_json(request):
    new_book_item = NewBook.objects.all
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