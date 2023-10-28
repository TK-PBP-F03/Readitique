from django.urls import path
from addbuku.views import add_buku, get_filtered, get_newbook_json, add_newbook_ajax

app_name = 'addbuku'
urlpatterns = [
    path('',add_buku,name='add_buku'),
    path('search/', get_filtered, name="get-filtered"),
    path('get-newbook', get_newbook_json, name='get_newbook_json'),
    path('add-newbook-ajax', add_newbook_ajax, name='add_newbook_ajax')
]