from django.urls import path

from .views import *

app_name = 'transaksipembelianaset'

urlpatterns = [
    path('listtransaksi', listtransaksi, name='listtransaksi'),
    path('buattransaksi', buattransaksi, name='buattransaksi')
]