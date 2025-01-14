# apps/blog/views.py

# Django modules
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse

# Third party
import json

# My modules
from blog.forms import BlogPostModelForm
from blog.models import Tag, BlogPost, Category, UserPostFav
from account.models import Profile

# Create your views here.


# ///////////////////////// home_view /////////////////////////
def home_view(request):
    # posts_latest = BlogPost.objects.filter(is_active=True).order_by('-created_at')
    posts_latest = BlogPost.objects.filter(is_active=True) #.order_by('-created_at')
    posts_trend = posts_latest.order_by('-view_count')[:6]
    tags = Tag.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    context = dict(
        posts_latest=posts_latest,
        posts_trend=posts_trend,
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


# ///////////////////////// post_edit_view /////////////////////////
def post_edit_view(request, post_slug):

    post = get_object_or_404(BlogPost, slug=post_slug)

    # If unknown user
    if not post.user == request.user:
        messages.warning(request, 'You cannot edit this post information')
        return redirect('blog:home_view')

    # Click post title to edit
    title = post.title
    form = BlogPostModelForm(instance=post)

    # Handling POST request
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES or None, instance=post)

        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            tags = json.loads(form.cleaned_data.get('tag'))
            for item in tags:
                tag_item, created = Tag.objects.get_or_create(title=item.get('value').lower())
                tag_item.is_active = True
                tag_item.save()
                f.tag.add(tag_item)

            messages.success(request, "Your blog post has been edited successfully..")
            return redirect('blog:home_view')
            
    context = dict(
        title=title,
        form=form,
    )
    return render(request, 'blog/update_blog_post.html', context)
# ///////////////////////// post_edit_view /////////////////////////


# ///////////////////////// posts_by_user_view /////////////////////////
def posts_by_user_view(request, user_slug):
    profile         = get_object_or_404(Profile, slug=user_slug)
    posts_by_user   = BlogPost.objects.filter(user=profile.user, is_active=True)
    context = dict(
        profile=profile,
        posts_by_user=posts_by_user,
    )
    return render(request, 'blog/posts_by_user.html', context)
# ///////////////////////// posts_by_user /////////////////////////


# ///////////////////////// post_detail_view /////////////////////////
def post_detail_view(request, user_slug, post_slug):
    post = get_object_or_404(BlogPost, slug=post_slug, is_active=True)
    post.view_count += 1
    post.save()
    context = dict(
        post=post,
    )
    return render(request, 'blog/post_detail.html', context)
# ///////////////////////// post_detail_view /////////////////////////


# ///////////////////////// posts_by_category_view /////////////////////////
def posts_by_category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts_by_category   = BlogPost.objects.filter(category=category, is_active=True)
    context = dict(
        category=category,
        posts_by_category=posts_by_category,
    )
    return render(request, 'blog/posts_by_category.html', context)
# ///////////////////////// posts_by_category_view /////////////////////////


# ///////////////////////// posts_by_tag_view /////////////////////////
def posts_by_tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts_by_tag = BlogPost.objects.filter(tag=tag)
    context = dict(
        tag=tag,
        posts_by_tag=posts_by_tag
    )
    return render(request, 'blog/posts_by_tag.html', context)
# ///////////////////////// posts_by_tag_view /////////////////////////


# ///////////////////////// fav_update_view /////////////////////////
def fav_update_view(request):
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, slug=request.POST.get('slug'))
        if post:
            post_fav, created = UserPostFav.objects.get_or_create(
                user=request.user,
                post=post,
            )
            if not created:
                post_fav.is_deleted = not post_fav.is_deleted
                post_fav.save()
    return JsonResponse({"status": "OK"})
# ///////////////////////// fav_update_view /////////////////////////
