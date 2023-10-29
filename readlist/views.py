
from django.shortcuts import redirect, render
from main.models import Book
from rprofile.models import UserProfile

def book_kosong(request):
    context = {
    }
    return render(request,'readlist.html',context)
def book_list(request, username):
    user_profile = UserProfile.objects.get(user__username=username)
    books = user_profile.favorite_books.all()
    context = {
        'user_profile': user_profile,
        'books': books,
    }
    return render(request, 'readlist.html', context)

def book_delete(request, pk):
    username = request.user.username
    user_profile = UserProfile.objects.get(user__username=username)
    book = Book.objects.get(pk=pk)
    user_profile.favorite_books.remove(book)
    
    
    return redirect("readlist:book_list", username=username)