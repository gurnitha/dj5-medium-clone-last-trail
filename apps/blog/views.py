# apps/blog/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib import messages

# Third party
import json

# My modules
from blog.forms import BlogPostModelForm
from blog.models import Tag, BlogPost, Category 

# Create your views here.


# ///////////////////////// home_view /////////////////////////
def home_view(request):
    # posts_latest = BlogPost.objects.filter(is_active=True).order_by('-created_at')
    posts_latest = BlogPost.objects.filter(is_active=True) #.order_by('-created_at')
    tags = Tag.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    context = dict(
        posts_latest=posts_latest,
        categories=categories,
        tags=tags,
    )
    return render(request, 'blog/index.html', context)
# ///////////////////////// home_view /////////////////////////


# ///////////////////////// create_blog_post_view /////////////////////////
def create_blog_post_view(request):

    # Handling GET request
    form = BlogPostModelForm()
    
    # Handling POST request
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            # print(form.cleaned_data)
            f.user = request.user
            f.save()

            # Handling ManyToMany relationship between tag and blogpost
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                # tag_item, created = models.Tag.objects.get_or_create(title=item.get('value'))
                tag_item, created = Tag.objects.get_or_create(title=item.get('value').lower())
                tag_item.is_active = True
                tag_item.save()
                f.tag.add(tag_item)

            # If post created, send messages and redirect to the home page
            messages.success(request, "Your blog post has been successfully saved.")
            return redirect('blog:home_view')
    
    context = dict(
        form=form
    )

    return render(request, 'blog/create_blog_post.html', context)
# ///////////////////////// create_blog_post_view /////////////////////////