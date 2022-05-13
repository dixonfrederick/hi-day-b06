from django.urls import path

from .views import *

app_name = 'histori_produksi'

urlpatterns = [
    path('historiprodukmakanan', historiProdukMakanan, name='historiProdukMakanan'),
]