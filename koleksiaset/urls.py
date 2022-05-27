from django.urls import path

from .views import *

app_name = 'koleksiaset'

urlpatterns = [
    path('listkoleksi', listkoleksi, name='listkoleksi'),

    path('listkoleksi_dekorasi', listkoleksi_dekorasi, name='listkoleksi_dekorasi'),
    path('listkoleksi_bibittanaman', listkoleksi_bibittanaman, name='listkoleksi_bibittanaman'),
    path('listkoleksi_kandang', listkoleksi_kandang, name='listkoleksi_kandang'),
    path('listkoleksi_hewan', listkoleksi_hewan, name='listkoleksi_hewan'),
    path('listkoleksi_alatproduksi', listkoleksi_alatproduksi, name='listkoleksi_alatproduksi'),
    path('listkoleksi_petaksawah', listkoleksi_petaksawah, name='listkoleksi_petaksawah')
]