from django.urls import path

from main.views import create_book, show_json, show_main, show_xml

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-book', create_book, name='create_book'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
]