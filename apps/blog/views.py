# apps/blog/views.py

# Django modules
from django.shortcuts import render

# My modules
from blog.forms import BlogPostModelForm

# Create your views here.

# ///////////////////////// home_view /////////////////////////
def home_view(request):
    return render(request, 'blog/index.html')
# ///////////////////////// home_view /////////////////////////


# ///////////////////////// create_blog_post_view /////////////////////////
def create_blog_post_view(request):

    # Handling GET request
    form = BlogPostModelForm()
    context = dict(
        form=form
    )
    return render(request, 'blog/create_blog_post.html', context)
# ///////////////////////// create_blog_post_view /////////////////////////