# apps/account/urls.py

# django modules
from django.urls import path

# my modules
from account import views 

# app name
app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('favs/', views.user_fav_view, name='user_fav_view'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit_view'),
    path("logout/", views.logout_view, name="logout_view"),
    path("register/", views.register_view, name="register_view"),
]