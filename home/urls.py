from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('registeradmin', views.registeradmin, name='registeradmin'),
    path('registerpengguna', views.registerpengguna, name='registerpengguna'),
    path('login', views.login, name='login')    
]