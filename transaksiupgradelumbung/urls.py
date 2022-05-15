from django.urls import path

from .views import *
from home.views import home

app_name = 'transaksiupgradelumbung'

urlpatterns = [
    path('home', home, name='home'),
    path('createtransaksiupgradelumbungpengguna', createtransaksiupgradelumbungpengguna, name='createtransaksiupgradelumbungpengguna'),
    path('readtransaksiupgradelumbungadmin', readtransaksiupgradelumbungadmin, name='readtransaksiupgradelumbungadmin'),
    path('readtransaksiupgradelumbungpengguna', readtransaksiupgradelumbungpengguna, name='readtransaksiupgradelumbungpengguna'),
]