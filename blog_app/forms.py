from django import forms
from django.core.validators import ValidationError

class ContactusForm(forms.Form):
    BIRTH_YEAR_CHOICES = ['1980','1981','1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES , attrs={'class':'form-control'}))
    name = forms.CharField(max_length=8,label='your name')
    text = forms.CharField(max_length=8 , label='your message')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if 'a' in name:
            self.add_error('name','a can not in this field')
        if name == text :
            raise ValidationError('name and text are same', code='name_text_same')
        
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if 'a' in name:
    #         raise ValidationError('a can not use at this field', code='a_in_name')  
    #     return name  
        


