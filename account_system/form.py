from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model = AccountModel
        fields = ['name','email','password']
        