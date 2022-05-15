from django.urls import path

from .views import *

app_name = 'aset'

urlpatterns = [
    path('listaset', listaset, name='listaset'),
    path('buataset', buataset, name='buataset'),
]