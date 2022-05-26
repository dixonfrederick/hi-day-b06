from django.urls import path

from .views import *

app_name = 'aset'

urlpatterns = [
    path('listaset', listaset, name='listaset'),
    path('buataset', buataset, name='buataset'),

    path('listaset_dekorasi', listaset_dekorasi, name='listaset_dekorasi'),
    path('listaset_bibittanaman', listaset_bibittanaman, name='listaset_bibittanaman'),
    path('listaset_kandang', listaset_kandang, name='listaset_kandang'),
    path('listaset_hewan', listaset_hewan, name='listaset_hewan'),
    path('listaset_alatproduksi', listaset_alatproduksi, name='listaset_alatproduksi'),
    path('listaset_petaksawah', listaset_petaksawah, name='listaset_petaksawah')
]