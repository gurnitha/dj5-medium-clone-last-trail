# apps/account/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Third party apps
from slugify import slugify

# My modules
from account.models import Profile
from account.forms import ProfileModelForm
from blog.models import BlogPost

# Create your views here.

# ///////////////////////// user_fav_view /////////////////////////
def user_fav_view(request):
    ids = request.user.userpostfav_set.filter(is_deleted=False).values_list('post_id', flat=True).order_by('-updated_at')
    context = dict(
        title="Favorilerim",
        favs=BlogPost.objects.filter(id__in=ids, is_active=True)
    )
    return render(request, 'blog/posts_fav.html', context)
# ///////////////////////// user_fav_view /////////////////////////


# ///////////////////////// login_view /////////////////////////
def login_view(request):

    # The logged-in user goes directly to the main page.
    if request.user.is_authenticated:
        messages.info(request, f"{request.user.username } You've logged in before.. ")
        return redirect('blog:home_view')

    # context
    context = dict()

    # Handling POST request
    if request.method == "POST":
        # Get username and password from the form instance
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)

        if len(username) < 5 or len(password) < 5:
            messages.warning(request, f'Please Enter the username and password correctly. It should not be less than 5 characters.')
            return redirect('account:login_view')

        # Authenticate suer
        user = authenticate(request, username=username, password=password)
        # If user exists
        if user is not None:
            login(request, user)
            # Let's make it clear to the user that you are logged in!
            messages.success(request, f'{request.user.username } You are logged in')
            # Redirect user ot home page
            return redirect('blog:home_view')

    return render(request, 'account/login.html', context)
# ///////////////////////// login_view /////////////////////////


# ///////////////////////// logout_view /////////////////////////
def logout_view(request):
    messages.info(request, f'{request.user.username } Logged out successfully')
    logout(request)
    return redirect('blog:home_view')
# ///////////////////////// logout_view /////////////////////////


# ///////////////////////// register_view /////////////////////////
def register_view(request):

    context = dict()

    # Handling POST request
    if request.method == "POST":

        # Get instances from the submited form
        post_info           = request.POST
        email               = post_info.get('email')
        email_confirm       = post_info.get('email_confirm')
        first_name          = post_info.get('first_name')
        last_name           = post_info.get('last_name')
        password            = post_info.get('password')
        password_confirm    = post_info.get('password_confirm')
        instagram           = post_info.get('instagram')
        
        # Validate firts_name, last_name, email, and password: at least 3 characters
        if len(first_name) < 3 or len(last_name) < 3 or len(email) < 3 or len(password) < 3: 
            messages.warning(request, "The information must consist of at least 3 characters.")
            return redirect('account:register_view')

        # Validate email and email confirm
        if email != email_confirm:
            messages.warning(request, "Please enter your email information correctly.")
            return redirect('account:register_view')

        # Validate password and password confirm
        if password != password_confirm:
            messages.warning(request, "Please enter the password information correctly.")
            return redirect('account:register_view')
        
        # Create username: use the email as the username
        user, created = User.objects.get_or_create(username=email)
        # If user already exsists in the db: log the user in and redirect user to the home page
        if not created:
            user_login = authenticate(request, username=email, password=password)
            if user is not None:
                messages.success(request, "You have already registered. You have been redirected to the main page.")
                # User login
                login(request, user_login)
                return redirect('blog:home_view')
            messages.warning(request, f'{email} , This email address is registered in the system, please login')
            return redirect('account:login_view')

        # User identity: Use email, first name, last name, and password as the USER's identities        
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)

        # Create user profile
        profile, profile_created = Profile.objects.get_or_create(user=user)
        profile.instagram = instagram
        profile.slug = slugify(f"{first_name}-{last_name}")
        user.save()
        profile.save()

        # If profile created: send message to user, log the user in, and redirect user to the home page
        messages.success(request, f'{user.first_name} You have been registered in the system..')
        user_login = authenticate(request, username=email, password=password)
        login(request, user_login)
        return redirect('blog:home_view')

    return render(request, 'account/register.html', context)
# ///////////////////////// register_view /////////////////////////


# ///////////////////////// profile_edit_view /////////////////////////
def profile_edit_view(request):
    user = request.user
    initial_data = dict(
        first_name = user.first_name,
        last_name = user.last_name,
    )
    form = ProfileModelForm(instance=user.profile, initial=initial_data)

    if request.method == "POST":
        form = ProfileModelForm(
            request.POST or None,
            request.FILES or None,
            instance=user.profile
        )
        if form.is_valid():
            f = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            f.save()
            messages.success(request, 'Profile updated successfully..')
            return redirect('account:profile_edit_view')
        

    title = "Profile update :"
    context = dict(
        form=form,
        title=title,
    )

    return render(request, 'account/profile_edit.html', context)
# ///////////////////////// profile_edit_view /////////////////////////
