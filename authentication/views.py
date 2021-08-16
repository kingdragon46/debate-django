from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib import messages
from app import views
from .models import *

# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        print('email is', request.POST)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user:
                print('User is authentic')
            else:
                print('Unauthenticated')
            
            if user is not None :
                print('User is authentic1')
                login(request, user)
                return redirect("home/")
            else:
                msg = 'Invalid credentials'  
        else:
            msg = 'Error validating the form'

    return render(request, "login.html", {"form": form, "msg" : msg})



def register_user(request):
    
    msg     = None
    success = False

    form = SignUpForm()
    if request.method == 'POST':
        print('In post')
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('In valid')
            user = form.save()
            email = form.cleaned_data.get('email')
            print('User: ', user)
            messages.success(request, 'Account is created for ' + email)
            return redirect("login/")
            
        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    context =  {"form": form, "msg" : msg, "success" : success }

    html_template = loader.get_template('register.html')
    return HttpResponse(html_template.render(context, request))