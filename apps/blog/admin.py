# apps/blog/admin.py

# Django modules
from django.contrib import admin

# My modules
from blog.models import Category, Tag, BlogPost 

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass