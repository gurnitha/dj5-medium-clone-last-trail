# apps/blog/forms.py

# Django modules
from django import forms

# My modules
from blog.models import BlogPost

# Create your model forms here.


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]