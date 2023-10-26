from django.urls import path
from review import views

app_name = "review"

urlpatterns = [
  path('', views.show_reviews, name="reviews"),
]