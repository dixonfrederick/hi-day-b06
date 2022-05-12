from django.urls import path

from .views import *

app_name = 'home'

urlpatterns = [
    path('', login, name='login'),
    path('home', index, name='index'),
    path('logout', logout, name='logout'),
    path('registeradmin', registeradmin, name='registeradmin'),
    path('registerpengguna', registerpengguna, name='registerpengguna'),

]