from django.urls import path

from .views import *

app_name = 'transaksipembelianaset'

urlpatterns = [
    path('readtransaksipembelianasetadmin', readtransaksipembelianasetadmin, name='readtransaksipembelianasetadmin'),
    path('createtransaksipembelianasetpengguna', createtransaksipembelianasetpengguna, name='createtransaksipembelianasetpengguna'),
    path('readtransaksipembelianasetpengguna', readtransaksipembelianasetpengguna, name='readtransaksipembelianasetpengguna')
]