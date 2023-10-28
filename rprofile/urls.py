from django.urls import path

from rprofile import views

app_name = 'rprofile'

urlpatterns = [
  path('rprofile/', views.profile, name="profile"),
  path('bookofchoice/', views.bookofchoice, name='bookofchoice'),
  path('update_email/', views.update_email, name='update_email'),
  path('update_phone/', views.update_phone, name='update_phone'),
  path('profile/edit_book/<int:id>/', views.edit_book, name='edit_book'),
  path('json/', views.show_json, name='show_json'), 
  path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
  path('rprofile/update_phone_number/', views.update_phone_number, name='update_phone_number'),
  path('rprofile/not_login/', views.not_login, name='not_login'),
 
  

]