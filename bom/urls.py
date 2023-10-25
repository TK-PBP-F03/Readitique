from django.urls import path
from . import views

app_name = 'bom'

urlpatterns = [
    path('', views.show_top_books, name='show_top_books'),
    path('increment_count/<int:book_id>/', views.increment_count, name='increment_count'),
    path('reset_counts/', views.reset_counts, name='reset_counts'),
]