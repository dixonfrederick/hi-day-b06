import email
from collections import namedtuple
import imp
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError, InterfaceError
from .forms import *
from django.utils import timezone

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def createtransaksiupgradelumbungpengguna(request):
    # form = CreateTransaksiUpgradeLumbungPenggunaForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    userEmail = request.session['email']
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("SELECT * FROM LUMBUNG WHERE LUMBUNG.EMAIL = %s", [userEmail])
    result = cursor.fetchall()
    level = (result[0])[1]
    kapasitas = (result[0])[2]
    now = timezone.now()
    if (request.method == 'POST'):
        # waktu = form.cleaned_data['waktu_upgrade']
        # level = form.cleaned_data['level_lumbung']
        # kapasitas = form.cleaned_data['kapasitas_lumbung']
        # biaya = form.cleaned_data['biaya_upgrade']
        try:
            cursor.execute("INSERT INTO TRANSAKSI_UPGRADE_LUMBUNG (email,waktu) VALUES (%s,%s)", [userEmail,now])
            cursor.execute("UPDATE LUMBUNG SET LEVEL = LEVEL + 1, KAPASITAS_MAKSIMAL = KAPASITAS_MAKSIMAL + 50 WHERE EMAIL = %s", [userEmail])
            cursor.execute("SET SEARCH_PATH TO public")
            return redirect("/transaksiupgradelumbung/readtransaksiupgradelumbungpengguna")
        except Exception as error:
            print(error)
    else:
        return render(request, 'transaksiupgradelumbung/createTransaksiUpgradeLumbungPengguna.html', {'level':level, 'kapasitas':kapasitas})

def readtransaksiupgradelumbungadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session['email']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT EMAIL, WAKTU FROM TRANSAKSI_UPGRADE_LUMBUNG WHERE TRANSAKSI_UPGRADE_LUMBUNG.EMAIL IN (SELECT PENGGUNA.EMAIL FROM PENGGUNA);""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'transaksiupgradelumbung/readTransaksiUpgradeLumbungAdmin.html', {'result':result})

def readtransaksiupgradelumbungpengguna(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT WAKTU FROM TRANSAKSI_UPGRADE_LUMBUNG WHERE EMAIL = %s;""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'transaksiupgradelumbung/readTransaksiUpgradeLumbungPengguna.html', {'result':result})
