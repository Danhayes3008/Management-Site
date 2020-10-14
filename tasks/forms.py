from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class taskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'deadline']
        widgets = {
            'deadline': DateInput()
        }
        
        