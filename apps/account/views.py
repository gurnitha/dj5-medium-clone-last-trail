# apps/account/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

# ///////////////////////// login_view /////////////////////////
def login_view(request):
    return render(request, 'account/login.html')
# ///////////////////////// login_view /////////////////////////