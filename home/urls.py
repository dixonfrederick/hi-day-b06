from django.urls import path

from .views import *

app_name = 'home'

urlpatterns = [
    path('', login, name='login'),
    path('logout', logout, name='logout'),
    path('home', home, name='home'),
    path('registeradmin', registeradmin, name='registeradmin'),
    path('registerpengguna', registerpengguna, name='registerpengguna'),

]