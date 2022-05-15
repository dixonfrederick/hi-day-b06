from django.urls import path

from .views import *

app_name = 'koleksiaset'

urlpatterns = [
    path('listkoleksi', listkoleksi, name='listkoleksi')
]