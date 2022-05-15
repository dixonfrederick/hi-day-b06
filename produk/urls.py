from django.urls import path

from .views import *

app_name = 'produk'

urlpatterns = [
    path('listproduk', listProduk, name='listProduk'),
    path('buatproduk', buatProduk, name='buatProduk'),
    path('listproduksi', listProduksi, name='listProduksi'),
    path("detailproduksi/<makanan>", detailProduksi, name="detailProduksi"),
    path('buatproduksi', buatProduksi, name='buatProduk'),
]