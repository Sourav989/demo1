from django import forms
from .models import *

class  JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company', 'position', 'status', 'link', 'notes', 'resume']