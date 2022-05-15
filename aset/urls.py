from django.urls import path

from .views import *

app_name = 'aset'

urlpatterns = [
    path('createasetadmin', createasetadmin, name='createasetadmin'),
    path('readasetadmin', readasetadmin, name='readasetadmin'),
    path('updateasetadmin', updateasetadmin, name='updateasetadmin'),
    path('deleteasetadmin', deleteasetadmin, name='deleteasetadmin'),
    path('readasetpengguna', readasetpengguna, name='readasetpengguna')
]