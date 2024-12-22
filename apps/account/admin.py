# apps/accounts/admin.py

# Django modules
from django.contrib import admin

# My modules
from account.models import Profile

# Register your models here.

admin.site.register(Profile)