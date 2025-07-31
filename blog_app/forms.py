from django import forms

class ContactusForm(forms.Form):
    name = forms.CharField(max_length=8,label='your name')
    text = forms.CharField(max_length=8 , label='your message')
