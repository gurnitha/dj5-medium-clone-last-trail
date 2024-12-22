# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # account
    path('user/', include('account.urls', namespace='account')),
    # blog
    path('', include('blog.urls', namespace='blog')),
    # admin
    path('admin/', admin.site.urls),
]
