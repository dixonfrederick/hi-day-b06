from django.urls import path

from .views import *

app_name = 'produk'

urlpatterns = [
    path('listproduk', listProduk, name='listProduk'),
    path('buatproduk', buatProduk, name='buatProduk'),
    path('updateproduk/<id>', updateProduk, name='updateProduk'),
    path('deleteproduk/<id>', deleteProduk, name='deleteProduk'),
    path('listproduksi', listProduksi, name='listProduksi'),
    path('detailproduksi/<id_alat_produksi>/<id_produk_makanan>', detailProduksi, name='detailProduksi'),
    path('updateproduksi/<id_alat_produksi>/<id_produk_makanan>', updateProduksi, name='updateProduksi'),
    path('deleteproduksi/<id_alat_produksi>/<id_produk_makanan>', deleteProduksi, name='deleteProduksi'),
    path('buatproduksi', buatProduksi, name='buatProduksi'),
]