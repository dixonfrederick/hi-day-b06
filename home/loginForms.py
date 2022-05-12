from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models 

class LoginForm(forms.Form):
    email = forms.CharField(label='E-Mail Address', max_length=50)
    password = forms.CharField(label='Password', max_length=50)