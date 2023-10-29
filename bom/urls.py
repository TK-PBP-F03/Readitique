from django.urls import path
from bom import views
app_name = 'bom'

urlpatterns = [
    path('', views.show_top_books, name='show_top_books'),
    path('<str:username>/', views.user_books, name='show_user_books'),
    path('bom/create-ajax/', views.add_quotes_ajax, name='add_quotes_ajax'),
    path('bom/get-ajax/', views.get_top_quotes, name='get_top_quotes'),

    # path('increment_count/<int:book_id>/', views.increment_count, name='increment_count'),
    # path('reset_counts/', views.reset_counts, name='reset_counts'),
]