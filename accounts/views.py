from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}
    return render(request, 'login.html', context)
