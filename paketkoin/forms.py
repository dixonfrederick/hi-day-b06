from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models 

class CreatePaketKoinAdminForm(forms.Form):
    jumlah_koin = forms.CharField(label='Jumlah Koin')
    harga = forms.CharField(label='Harga')
