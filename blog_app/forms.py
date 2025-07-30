from django import forms

class ContactusForm(forms.Form):
    text = forms.CharField(max_length=300 , label='your message')
