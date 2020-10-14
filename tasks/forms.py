from django import forms
from .models import *

class taskForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Task
        fields = ['title']
        