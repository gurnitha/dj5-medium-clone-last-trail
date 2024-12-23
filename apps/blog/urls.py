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
    path('blog/post/<slug:post_slug>/edit/', views.post_edit_view, name='post_edit_view'),
    path('blog/post/<slug:user_slug>/', views.posts_by_user_view, name='posts_by_user_view'),
    path('blog/post/<slug:user_slug>/<slug:post_slug>/', views.post_detail_view, name='post_detail_view'),
    path('blog/category/<slug:category_slug>/', views.posts_by_category_view, name='posts_by_category_view'),
    path('blog/tag/<slug:tag_slug>/', views.posts_by_tag_view, name='posts_by_tag_view'),
    path('fav-update/', views.fav_update_view, name='fav_update_view'),
]