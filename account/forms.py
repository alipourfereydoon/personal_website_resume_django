from django import forms
from . models import Login
from django.contrib.auth import authenticate
from django.forms import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        user = authenticate(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError('information is not corresct' , code='invalid_info')
    
    
