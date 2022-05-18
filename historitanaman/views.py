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

def createhistoritanamanpengguna(request):
    form = CreateHistoriTanamanPenggunaForm(request.POST or None)
    context = {'form':form}
    return render(request, 'historitanaman/createHistoriTanamanPengguna.html',context)

def readhistoritanamanadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session['email']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT HISTORI_TANAMAN.EMAIL, HISTORI_TANAMAN.WAKTU_AWAL, HISTORI_PRODUKSI.WAKTU_SELESAI, HISTORI_PRODUKSI.JUMLAH, HISTORI_PRODUKSI.XP, PETAK_SAWAH.JENIS_TANAMAN FROM HISTORI_TANAMAN, HISTORI_PRODUKSI, PETAK_SAWAH WHERE HISTORI_TANAMAN.ID_BIBIT_TANAMAN = PETAK_SAWAH.ID_ASET AND EXISTS (SELECT EMAIL, WAKTU_AWAL FROM HISTORI_PRODUKSI WHERE HISTORI_PRODUKSI.EMAIL = HISTORI_TANAMAN.EMAIL AND HISTORI_PRODUKSI.WAKTU_AWAL = HISTORI_TANAMAN.WAKTU_AWAL);""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'historitanaman/readHistoriTanamanAdmin.html', {'result':result})

def readhistoritanamanpengguna(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT HISTORI_TANAMAN.WAKTU_AWAL, HISTORI_PRODUKSI.WAKTU_SELESAI, HISTORI_PRODUKSI.JUMLAH, HISTORI_PRODUKSI.XP, PETAK_SAWAH.JENIS_TANAMAN FROM HISTORI_TANAMAN, HISTORI_PRODUKSI, PETAK_SAWAH WHERE HISTORI_TANAMAN.ID_BIBIT_TANAMAN = PETAK_SAWAH.ID_ASET AND EXISTS (SELECT EMAIL, WAKTU_AWAL FROM HISTORI_PRODUKSI WHERE HISTORI_PRODUKSI.EMAIL = HISTORI_TANAMAN.EMAIL AND HISTORI_PRODUKSI.WAKTU_AWAL = HISTORI_TANAMAN.WAKTU_AWAL) AND HISTORI_TANAMAN.EMAIL = %s;""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'historitanaman/readHistoriTanamanPengguna.html', {'result':result})
