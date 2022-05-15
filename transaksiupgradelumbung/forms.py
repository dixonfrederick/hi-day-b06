from django.contrib.auth import forms
from django.forms import ModelForm, fields
from django import forms
from django.utils import timezone
from django.db import models
import datetime
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from . import models 

class CreateTransaksiUpgradeLumbungPenggunaForm(forms.Form):
    level_lumbung = forms.CharField(label='Level Lumbung')
    kapasitas_lumbung = forms.CharField(label='Kapasitas Lumbung')
    biaya_upgrade = forms.CharField(label='Biaya Upgrade')
    email_pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    waktu_upgrade = models.DateTimeField(auto_now_add=True)
