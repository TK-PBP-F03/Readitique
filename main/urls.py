from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
  path('', views.show_main, name="show-main"),
  path('search/', views.get_filtered, name="get-filtered"),
  path('login/', views.login_user, name="login"),
  path('logout/', views.logout_user, name="logout"),
  path('register/', views.register, name="register"),
]