from django.urls import path
from addbuku.views import add_buku, get_newbook_json, add_newbook_ajax, increment_votes, approve_book

app_name = 'addbuku'
urlpatterns = [
    path('',add_buku,name='add_buku'),
    path('get-newbook-json/', get_newbook_json, name='get_newbook_json'),
    path('add-newbook-ajax/', add_newbook_ajax, name='add_newbook_ajax'),
    path('increment-votes/<int:id>/', increment_votes, name='increment_votes'),
    path('approve-book/<int:id>/', approve_book, name='approve_book')
]