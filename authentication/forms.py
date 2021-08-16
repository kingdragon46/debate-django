# -*- encoding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from .models import *

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))


phone_regex = RegexValidator( regex = r'^\+?1?\d{9,10}$', message ="Phone number must be entered in the format +919999999999. Up to 10 digits allowed.")
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "First Name",                
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Last Name",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id" : "password1",
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id" : "password2",
                "placeholder" : "Re-enter Password",                
                "class": "form-control"
            }
        ))
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Phone Number",                
                "class": "form-control",
                "maxlength" : "10"
            }
        ))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'phone']


class UserForm(forms.ModelForm):
    """Form definition for User."""
    user_type = forms.ChoiceField(
        required=False,
        choices=user_choices,
        widget=forms.Select(
            attrs={
                # "placeholder" : "Product Name",                
                "class": "form-control",
                "name" : "user_type",
                "id" : "user_type"
            }
        ))

    is_banned = forms.BooleanField(
        required=False
        )
    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ['user_type', 'is_banned']
