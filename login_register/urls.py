from django.urls import path

from .views import *

app_name = 'login_register'

urlpatterns = [
    path('login', login, name='login'),
    path('registeradmin', registeradmin, name='registeradmin'),
    path('registerpengguna', registerpengguna, name='registerpengguna'),
]