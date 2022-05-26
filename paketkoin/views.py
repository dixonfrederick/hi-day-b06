import email
from collections import namedtuple
import imp
from pickletools import read_uint1
import re
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError, InterfaceError
from .forms import *
from .forms2 import *
from django.utils import timezone

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def createtransaksipembeliankoinpengguna(request, id):
    # form = CreateTransaksiPembelianKoinPenggunaForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    userEmail = request.session['email']
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("SELECT * FROM PAKET_KOIN WHERE PAKET_KOIN.JUMLAH_KOIN = %s", [id])
    result = cursor.fetchall()
    jumlah_koin = (result[0])[0]
    harga = (result[0])[1]
    now = timezone.now()
    if (request.method == 'POST'):
        # waktu = form.cleaned_data['waktu_pembelian']
        # jumlah = form.cleaned_data['jumlah']
        # cara_pembayaran = form.cleaned_data['cara_pembayaran']
        # paket_koin = form.cleaned_data['paket_koin']
        # total_biaya = form.cleaned_data['harga'] * form.cleaned_data['jumlah']
        if (request.POST['jumlah'] == "" or request.POST['cara_pembayaran'] == ""):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'paketkoin/createTransaksiPembelianKoinPengguna.html', {'message':message})
        else:
            total_biaya = request.POST['jumlah'] * harga
            cursor.execute("INSERT INTO TRANSAKSI_PEMBELIAN_KOIN (email,waktu,jumlah,cara_pembayaran,paket_koin,total_biaya) VALUES (%s,%s,%s,%s,%s,%s)", [userEmail,now,request.POST['jumlah'],request.POST['cara_pembayaran'],id,total_biaya])
        return redirect("/transaksipembeliankoin/readtransaksipembeliankoinpengguna")
    return render(request, 'paketkoin/createTransaksiPembelianKoinPengguna.html', {'jumlah_koin':jumlah_koin, 'harga':harga})

def createpaketkoinadmin(request):
    #form = CreatePaketKoinAdminForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    if (request.method == 'POST'):
        # jumlah_koin = form.cleaned_data['jumlah_koin']
        # harga = form.cleaned_data['harga']
        cursor.execute("SELECT JUMLAH_KOIN FROM PAKET_KOIN")
        result = cursor.fetchall()
        if (request.POST['jumlah_koin'] == "" or request.POST['harga'] == ""):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'paketkoin/createPaketKoinAdmin.html', {'message':message})
        elif (request.POST['jumlah_koin'] in str((result[0])[0])):
            message = "Paket koin sudah ada, harap masukkan yang berbeda"
            return render(request, 'paketkoin/createPaketKoinAdmin.html', {'message':message})
        else:
            id = request.POST['jumlah_koin']
            cursor.execute("INSERT INTO PAKET_KOIN (jumlah_koin,harga) VALUES (%s,%s)", [id, request.POST['harga']])
        return redirect('/paketkoin/readpaketkoinadmin')
    return render(request, 'paketkoin/createPaketKoinAdmin.html')

def deletepaketkoinadmin(request, id):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("SELECT * FROM PAKET_KOIN WHERE PAKET_KOIN.JUMLAH_KOIN = %s", [id])
    result = cursor.fetchall()
    jumlah_koin = (result[0])[0]
    if (request.method == 'POST'):
        cursor.execute("DELETE FROM PAKET_KOIN WHERE PAKET_KOIN.JUMLAH_KOIN = %s", [id])
        return redirect('/paketkoin/readpaketkoinadmin')
    return render(request, 'paketkoin/deletePaketKoinAdmin.html', {'jumlah_koin':jumlah_koin})

def updatepaketkoinadmin(request, id):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("SELECT * FROM PAKET_KOIN WHERE PAKET_KOIN.JUMLAH_KOIN = %s", [id])
    result = cursor.fetchall()
    jumlah_koin = (result[0])[0]
    if (request.method == 'POST'):
        if (request.POST['harga'] == ""):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render(request, 'paketkoin/updatePaketKoinAdmin.html', {'message':message})
        else:
            cursor.execute("UPDATE PAKET_KOIN SET HARGA = %s WHERE PAKET_KOIN.JUMLAH_KOIN = %s", [request.POST['harga'], id])
            return redirect('/paketkoin/readpaketkoinadmin')
    # form = UpdatePaketKoinAdminForm(request.POST or None)
    else:
        return render(request, 'paketkoin/updatePaketKoinAdmin.html', {'jumlah_koin':jumlah_koin})

def readpaketkoinadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT JUMLAH_KOIN, HARGA FROM PAKET_KOIN;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'paketkoin/readPaketKoinAdmin.html', {'result':result})

def readpaketkoinpengguna(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT JUMLAH_KOIN, HARGA FROM PAKET_KOIN;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'paketkoin/readPaketKoinPengguna.html', {'result':result})

