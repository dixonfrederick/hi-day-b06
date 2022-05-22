import email
from collections import namedtuple
import imp
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError, InterfaceError
from .forms import *

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def createtransaksipembeliankoinpengguna(request):
    form = CreateTransaksiPembelianKoinPenggunaForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    role = request.session['role']
    userEmail = request.session['email']
    if (form.is_valid() and request.method == 'POST'):
        waktu = form.cleaned_data['waktu_pembelian']
        jumlah = form.cleaned_data['jumlah']
        cara_pembayaran = form.cleaned_data['cara_pembayaran']
        paket_koin = form.cleaned_data['paket_koin']
        total_biaya = form.cleaned_data['harga'] * form.cleaned_data['jumlah']
        if ((waktu is not None) and (jumlah is not None) and (cara_pembayaran is not None) and (paket_koin is not None) and (total_biaya is not None)):
            try:
                cursor.execute("INSERT INTO TRANSAKSI_PEMBELIAN_KOIN (email,waktu,jumlah,cara_pembayaran,paket_koin,total_biaya) VALUES (%s,%s,%d,%s,%d,%d)", [userEmail,waktu,jumlah,cara_pembayaran,paket_koin,total_biaya])
                cursor.execute("SET SEARCH_PATH TO public")
                return redirect("/readtransaksipembeliankoinpengguna")
            except Exception as error:
                print(error)
        else:
            message = "Masih ada yang kosong"
            return render(request, 'transaksipembeliankoin/createTransaksiPembelianKoinPengguna.html', {'message':message})
    else:
        return render(request, 'transaksipembeliankoin/createTransaksiPembelianKoinPengguna.html', {'form':form})

def readtransaksipembeliankoinadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session['email']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT EMAIL, WAKTU, JUMLAH, CARA_PEMBAYARAN, PAKET_KOIN, TOTAL_BIAYA FROM TRANSAKSI_PEMBELIAN_KOIN WHERE TRANSAKSI_PEMBELIAN_KOIN.EMAIL IN (SELECT PENGGUNA.EMAIL FROM PENGGUNA);""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'transaksipembeliankoin/readTransaksiPembelianKoinAdmin.html', {'result':result})

def readtransaksipembeliankoinpengguna(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT WAKTU, JUMLAH, CARA_PEMBAYARAN, PAKET_KOIN, TOTAL_BIAYA FROM TRANSAKSI_PEMBELIAN_KOIN WHERE EMAIL = %s;""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'transaksipembeliankoin/readTransaksiPembelianKoinPengguna.html', {'result':result})
