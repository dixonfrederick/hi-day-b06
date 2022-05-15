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

class CreateTransaksiPembelianKoinPenggunaForm(forms.Form):
    paket_koin = forms.CharField(label='Paket Koin')
    harga = forms.CharField(label='Harga')
    jumlah = forms.CharField(label='Jumlah')
    cara_pembayaran = forms.CharField(label='Cara Pembayaran')
    email_pengguna = models.ForeignKey(User, on_delete=models.CASCADE)
    waktu_pembelian = models.DateTimeField(auto_now_add=True)
