from django.urls import path

from .views import *
from home.views import home

app_name = 'paketkoin'

urlpatterns = [
    path('home', home, name='home'),
    path('createpaketkoinadmin', createpaketkoinadmin, name='createpaketkoinadmin'),
    path('createtransaksipembeliankoinpengguna/<id>', createtransaksipembeliankoinpengguna, name='createtransaksipembeliankoinpengguna'),
    path('deletepaketkoinadmin/<id>', deletepaketkoinadmin, name='deletepaketkoinadmin'),
    path('readpaketkoinadmin', readpaketkoinadmin, name='readpaketkoinadmin'),
    path('readpaketkoinpengguna', readpaketkoinpengguna, name='readpaketkoinpengguna'),
    path('updatepaketkoinadmin/<id>', updatepaketkoinadmin, name='updatepaketkoinadmin'),
]