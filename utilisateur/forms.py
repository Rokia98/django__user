from django import forms
from .models import *


class UserForms(forms.Form):
    pseudo = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    created_at = forms.DateField()


class UserFormsModel(forms.ModelForm):
    class Meta:
        model = Users 
        fields = ["pseudo", "password"]
        


