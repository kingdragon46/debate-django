from django.forms import ModelForm
from django import forms
from .models import *



class newDebateForm(forms.ModelForm):
    """Form definition for Customer."""
    title = forms.CharField(
        required= True,
        widget=forms.TextInput(
            attrs={   
                "id" : "title" ,
                "name": "title",           
                "class": "form-control",
            }
        ))

    text = forms.CharField(
        required= True,
        widget=forms.Textarea(
            attrs={   
                "id" : "text" ,
                "name": "text",           
                "class": "form-control",
            }
        ))

    owner = forms.CharField(
        required= False,
        widget=forms.TextInput(
            attrs={   
                "id" : "owner" ,
                "name": "owner",           
                "class": "form-control",
            }
        ))

    class Meta:
        """Meta definition for Customerform."""
        model = Discussion
        fields = '__all__'