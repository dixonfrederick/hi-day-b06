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

def createtransaksiupgradelumbungpengguna(request):
    form = CreateTransaksiUpgradeLumbungPenggunaForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    role = request.session['role']
    userEmail = request.session['email']
    if (form.is_valid() and request.method == 'POST'):
        waktu = form.cleaned_data['waktu_upgrade']
        level = form.cleaned_data['level_lumbung']
        kapasitas = form.cleaned_data['kapasitas_lumbung']
        biaya = form.cleaned_data['biaya_upgrade']
        if ((waktu is not None) and (level is not None) and (kapasitas is not None) and (biaya is not None)):
            try:
                cursor.execute("INSERT INTO TRANSAKSI_UPGRADE_LUMBUNG (email,waktu) VALUES (%s,%s)", [userEmail,waktu])
                cursor.execute("UPDATE LUMBUNG SET (LEVEL = LEVEL + 1) AND (KAPASITAS_MAKSIMAL = KAPASITAS_MAKSIMAL + 50) WHERE EMAIL = %s AND LEVEL = %d AND KAPASITAS_MAKSIMAL = %d", [userEmail,level,kapasitas])
                cursor.execute("SET SEARCH_PATH TO public")
                return redirect("/readtransaksiupgradelumbungpengguna")
            except Exception as error:
                print(error)
        else:
            message = "Masih ada yang kosong"
            return render(request, 'transaksiupgradelumbung/createTransaksiUpgradeLumbungPengguna.html', {'message':message})
    else:
        return render(request, 'transaksiupgradelumbung/createTransaksiUpgradeLumbungPengguna.html', {'form':form})

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
