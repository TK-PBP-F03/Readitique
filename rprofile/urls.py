from django.urls import path

from rprofile import views

app_name = 'rprofile'

urlpatterns = [
  path('rprofile/', views.profile, name="profile"),
  path('bookofchoice/', views.bookofchoice, name='bookofchoice'),
  path('update_email/', views.update_email, name='update_email'),
  path('update_phone/', views.update_phone, name='update_phone'),
 
  

]