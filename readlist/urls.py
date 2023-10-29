from django.urls import path
from . import views

app_name = 'readlist'

urlpatterns = [
    path('',views.book_kosong,name='book_kosong'),
    path('<str:username>/',views.book_list,name='book_list'),
    path('<int:pk>/delete', views.book_delete , name='book_delete'),
]