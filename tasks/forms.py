from django import forms
from .models import *

class taskForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Task
        fields = ['name', 'user', 'status']
        