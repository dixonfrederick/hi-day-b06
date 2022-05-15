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

def createhistoritanamanpengguna(request):
    form = CreateHistoriTanamanPenggunaForm(request.POST or None)
    context = {'form':form}
    return render(request, 'historitanaman/createHistoriTanamanPengguna.html',context)

def readhistoritanamanadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH to public")
    role = request.session ['role']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("SELECT histori_produksi.Email, histori_produksi.Waktu_Awal, histori_produksi.Waktu_Selesai, histori_produksi.Jumlah, histori_produksi.XP FROM histori_produksi, histori_tanaman WHERE histori_produksi.Email = histori_tanaman.Email AND histori_produksi.Waktu_Awal = histori_tanaman.Waktu_Awal")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'historitanaman/readHistoriTanamanAdmin.html', {'result':result})

def readhistoritanamanpengguna(request):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH to public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("SELECT histori_produksi.Waktu_Awal, histori_produksi.Waktu_Selesai, histori_produksi.Jumlah, histori_produksi.XP FROM histori_produksi, histori_tanaman WHERE histori_produksi.Email = histori_tanaman.Email AND histori_produksi.Waktu_Awal = histori_tanaman.Waktu_Awal")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'historitanaman/readHistoriTanamanPengguna.html', {'result':result})
