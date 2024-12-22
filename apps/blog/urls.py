# apps/blog/urls.py

# django modules
from django.urls import path

# my modules
from blog import views 

# app name
app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home_view'),
]