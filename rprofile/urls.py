from django.urls import path

from rprofile import views

app_name = 'rprofile'

urlpatterns = [
  path('rprofile/', views.profile, name="profile"),
  path('bookofchoice/', views.bookofchoice, name='bookofchoice'),

]