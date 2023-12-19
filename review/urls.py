from django.urls import path
from review import views

app_name = "review"

urlpatterns = [
  path('', views.show_reviews, name="reviews"),
  path('<int:pk>/', views.book_review, name="book-review"), 
  path('<int:pk>/addreview/', views.create_review, name="create-review"),
  path('<int:pk>/get-review/', views.get_review_ajax, name="get-review"),
  path('reviews-json/', views.reviews_JSON, name="reviews-json"),
  path('<int:ik>/json/', views.book_reviews_JSON, name="book-review-json"),
  path('<int:ik>/create-flutter/', views.write_review_flutter, name="write-review-flutter")
]