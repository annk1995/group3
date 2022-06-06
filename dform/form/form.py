from dataclasses import fields
# from click import style
from django import forms


from .models import Snippet
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Fieldset


class ContactForm(forms.Form):
    ROLE_CHOICES=(
    ("Mgr", "Manager"),
    ("Emp", "Employee"),
    ("Admin", "Administrator"),
    ("Sup", "Supervisor"),
    )

    name =forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Username', 'style': 'max-width: 700px;'}))
    email =forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Your email', 'style': 'max-width: 700px;'}))
    roles= forms.ChoiceField(choices=ROLE_CHOICES ,widget=forms.Select(attrs={'class': 'form-control', 'placeholder':'Your role', 'style': 'max-width: 700px;'}))
    spirit_animal = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Your Spirt Animal', 'style': 'max-width: 700px;'}))
    date_created =forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Date created', 'style': 'max-width: 700px;'}))
    

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper =FormHelper
        self.helper.form_method ='post'

        self.helper.layout =Layout(
            
            'name',
            'email',
            'roles',
            'spirit_animal',
            'date_created',
            

            
            Submit('submit','submit',css_class='btn btn-primary',style="margin-left:200px; margin-top:10px;")




        )

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('name', 'email','spirit_animal','roles')
        labels = {
            'name': 'Username',
            'email': 'Email',
            'spirit_animal': 'Spirit Animal',
            'roles': 'Roles',
            
            }

        
      
    