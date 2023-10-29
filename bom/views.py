from pipes import quote
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from bom.models import Quotes
from rprofile.models import UserProfile
from main.models import Book
from django.shortcuts import redirect
from .forms import QuotesForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def increment_count(request, book_id):
    try:
        book = Book.objects.get(id=book_id+1)
        book.count_read += 1
        book.save()
        return JsonResponse({'count_read': book.count_read})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Buku tidak ditemukan'}, status=404)

def reset_counts(request):
    # Ambil semua buku
    books = Book.objects.all()
    # Reset jumlah pembaca ke 0 untuk setiap buku
    books.update(count_read=0)
    
    # Redirect kembali ke halaman utama atau halaman yang Anda inginkan
    return redirect('bom:show_top_books')

def rank_book(num_books=7):
    books = Book.objects.all().order_by('-count_read')[:num_books]
    return books

def show_top_books(request):
    top_books = rank_book()
    
    context = {
        'top_books': top_books,
        
    }
    return render(request, 'bom.html', context)

@login_required
def user_books(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    favorite_books = user_profile.favorite_books.all()
    top_books = rank_book()
    
    context = {
        'user_profile': user_profile,
        'favorite_books': favorite_books,
        'top_books': top_books,
    }
    return render(request, 'bom.html', context)

def get_top_quotes(request):
    quotes = Quotes.objects.all()
    quotes_list = [quote.quotes for quote in quotes]  # Mengambil teks quotes

    return JsonResponse({'quotes': [quotes_list[-1]]})


@login_required
@csrf_exempt
def add_quotes_ajax(request):
    if request.method == 'POST':
        quotes_form = QuotesForm(request.POST)
        print('tess')
        if quotes_form.is_valid():
            print('tess')
            quotes = request.POST.get("quotes")
            new_quotes = Quotes(user=request.user, quotes=quotes)
            new_quotes.save()

            return HttpResponse(b"CREATED", status=201)
        else:
            return HttpResponse(b"NOT FOUND", status=205)
    return HttpResponseNotFound()

