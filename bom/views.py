from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Book
from django.shortcuts import redirect
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