from django.urls import path
from . import views

app_name = 'readlist'
<<<<<<< HEAD

urlpatterns = [
    path('',views.book_kosong,name='book_kosong'),
    path('<str:username>/',views.book_list,name='book_list'),
    path('<int:pk>/delete', views.book_delete , name='book_delete'),
=======
urlpatterns = [
    path('',views.book_list,name='book_list')
>>>>>>> 93d17ac0b68397e7c1640379ec5bef22acc339a9
]