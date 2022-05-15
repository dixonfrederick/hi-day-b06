from django.urls import path

from .views import *

app_name = 'koleksiaset'

urlpatterns = [
    path('readkoleksiasetadmin', readkoleksiasetadmin, name='readkoleksiasetadmin'),
    path('readkoleksiasetpengguna', readkoleksiasetpengguna, name='readkoleksiasetpengguna')
]