from django.urls import path

from .views import *
from home.views import home

app_name = 'historitanaman'

urlpatterns = [
    path('home', home, name='home'),
    path('createhistoritanamanpengguna', createhistoritanamanpengguna, name='createhistoritanamanpengguna'),
    path('readhistoritanamanadmin', readhistoritanamanadmin, name='readhistoritanamanadmin'),
    path('readhistoritanamanpengguna', readhistoritanamanpengguna, name='readhistoritanamanpengguna'),
]