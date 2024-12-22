# apps/blog/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# ///////////////////////// home_view /////////////////////////
def home_view(request):
    return render(request, 'blog/index.html')
# ///////////////////////// home_view /////////////////////////