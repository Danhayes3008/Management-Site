from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('add_task/', addTask, name="addTask"),
]