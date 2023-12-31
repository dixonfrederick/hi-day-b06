"""hi_day_b06 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from login_register.views import login as index
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_register/', include('login_register.urls')),
    path('home/', include('home.urls')),
    path('produk/', include('produk.urls')),
    path('histori_produksi/', include('histori_produksi.urls')),
    path('paketkoin/', include('paketkoin.urls')),
    path('transaksipembeliankoin/', include('transaksipembeliankoin.urls')),
    path('transaksiupgradelumbung/', include('transaksiupgradelumbung.urls')),
    path('lumbung/', include('lumbung.urls')),
    path('historitanaman/', include('historitanaman.urls')),
    path('aset/', include('aset.urls')),
    path('koleksiaset/', include('koleksiaset.urls')),
    path('transaksipembelianaset/', include('transaksipembelianaset.urls')),
    re_path(r'^$', index, name='index'),
]
