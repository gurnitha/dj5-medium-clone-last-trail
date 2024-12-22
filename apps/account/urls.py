# apps/account/urls.py

# django modules
from django.urls import path

# my modules
from account import views 

# app name
app_name = 'account'

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
]