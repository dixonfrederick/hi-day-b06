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

class CreateHistoriTanamanPenggunaForm(forms.Form):
    bibit_tanaman = forms.CharField(label='Bibit Tanaman')
    jumlah = forms.CharField(label='Jumlah')
    xp = forms.CharField(label='XP')
    waktu_awal = models.DateTimeField(auto_now_add=True)
    waktu_selesai = waktu_awal
