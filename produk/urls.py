from django.urls import path

from .views import *

app_name = 'produk'

urlpatterns = [
    path('listproduk', listProduk, name='listProduk'),
]