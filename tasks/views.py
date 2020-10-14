from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from .forms import *

# Create your views here.
def addTask(request):
    if request.method == 'POST':
        task_form = taskForm(request.POST)
        
        if task_form.is_valid():
            task_form.save()
            messages.success(request, "Your task has been added")
            return redirect('index')
    else:
        task_form = taskForm()
    return render(request, 'addTask.html', {'task_form': task_form})