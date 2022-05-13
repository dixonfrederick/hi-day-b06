from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models 

class CreateUserForm2(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password2', 'password']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm2, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].widget.attrs['placeholder'] = 'Nama Area Pertanian'
