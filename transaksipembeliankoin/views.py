from collections import namedtuple
import imp
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError, InterfaceError
from .forms import *

# Create your views here.
role = ""

def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def createtransaksipembeliankoinpengguna(request):
    form = CreateTransaksiPembelianKoinPenggunaForm(request.POST or None)
    context = {'form':form}
    return render(request, 'transaksipembeliankoin/createTransaksiPembelianKoinPengguna.html',context)

def readtransaksipembeliankoinadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH to public")
    role = request.session ['role']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("SELECT transaksi_pembelian_koin.Email, transaksi_pembelian_koin.Waktu, transaksi_pembelian_koin.Jumlah, transaksi_pembelian_koin.Cara_Pembayaran, transaksi_pembelian_koin.Paket_Koin, transaksi_pembelian_koin.Total_Biaya FROM transaksi_pembelian_koin")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'transaksipembeliankoin/readTransaksiPembelianKoinAdmin.html', {'result':result})

def readtransaksipembeliankoinpengguna(request):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH to public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("SELECT transaksi_pembelian_koin.Waktu, transaksi_pembelian_koin.Jumlah, transaksi_pembelian_koin.Cara_Pembayaran, transaksi_pembelian_koin.Paket_Koin, transaksi_pembelian_koin.Total_Biaya FROM transaksi_pembelian_koin")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'transaksipembeliankoin/readTransaksiPembelianKoinPengguna.html', {'result':result})
