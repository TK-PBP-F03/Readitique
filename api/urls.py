
from django.urls import path
from .views import BookListCreateView, BookDetailView, UserProfileListCreateView, user_profiles


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
  #  path('user_profiles/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),
    path('user_profiles/', user_profiles, name='user_profiles'),
]