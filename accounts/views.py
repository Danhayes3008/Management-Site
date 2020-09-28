from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def login(request):
    login_form = LoginForm(request.POST)
    context = {'login_form': login_form}
    return render(request, 'login.html', context)