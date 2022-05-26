from django.urls import path

from .views import *
from home.views import home

app_name = 'transaksipembeliankoin'

urlpatterns = [
    path('home', home, name='home'),
    path('readtransaksipembeliankoinadmin', readtransaksipembeliankoinadmin, name='readtransaksipembeliankoinadmin'),
    path('readtransaksipembeliankoinpengguna', readtransaksipembeliankoinpengguna, name='readtransaksipembeliankoinpengguna'),
]