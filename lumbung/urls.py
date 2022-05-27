from django.urls import path

from .views import *
from home.views import home

app_name = 'lumbung'

urlpatterns = [
    path('home', home, name='home'),
    path('readlumbung', readlumbung, name='readlumbung'),
]