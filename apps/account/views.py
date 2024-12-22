# apps/account/views.py

# Django modules
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

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