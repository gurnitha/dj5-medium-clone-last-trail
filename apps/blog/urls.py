# apps/blog/urls.py

# django modules
from django.urls import path

# my modules
from blog import views 

# app name
app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('blog/create/', views.create_blog_post_view, name='create_blog_post_view'),
    path('blog/post/<slug:user_slug>/', views.posts_by_user_view, name='posts_by_user_view'),
]