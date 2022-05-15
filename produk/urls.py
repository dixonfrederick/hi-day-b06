from django.urls import path

from .views import *

app_name = 'produk'

urlpatterns = [
    path('listproduk', listProduk, name='listProduk'),
    path('buatproduk', buatProduk, name='buatProduk'),
    path('listproduksi', listProduksi, name='listProduksi'),
    path('buatproduk', buatProduksi, name='buatProduk'),
]