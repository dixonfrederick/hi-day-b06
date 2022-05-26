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
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    userEmail = request.session['email']
    if (form.is_valid() and request.method == 'POST'):
        bibit = form.cleaned_data['bibit_tanaman']
        jumlah = form.cleaned_data['jumlah']
        xp = form.cleaned_data['xp']
        waktu_awal = form.cleaned_data['waktu_awal']
        waktu_selesai = form.cleaned_data['waktu_selesai']
        if ((bibit is not None) and (jumlah is not None) and (xp is not None) and (waktu_awal is not None) and (waktu_selesai is not None)):
            try:
                cursor.execute("INSERT INTO HISTORI_TANAMAN (email,waktu_awal,id_bibit_tanaman) VALUES (%s,%s, (SELECT BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN.ID_BIBIT_TANAMAN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN, PRODUK WHERE PRODUK.ID = BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN.ID_HASIL_PANEN AND PRODUK.NAMA = %s))", [userEmail,waktu_awal,bibit])
                cursor.execute("INSERT INTO HISTORI_PRODUKSI (email,waktu_awal,waktu_selesai,jumlah,xp) VALUES (%s,%s,%s,%d,%d)", [userEmail,waktu_awal,waktu_selesai,jumlah,xp])
                cursor.execute("SET SEARCH_PATH TO public")
                return redirect("/readhistoritanamanpengguna")
            except Exception as error:
                print(error)
        else:
            message = "Masih ada yang kosong"
            return render(request, 'historitanaman/createHistoriTanamanPengguna.html', {'message':message})
    else:
        return render(request, 'historitanaman/createHistoriTanamanPengguna.html', {'form':form})

def readhistoritanamanadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session['email']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT HISTORI_TANAMAN.EMAIL, HISTORI_TANAMAN.WAKTU_AWAL, HISTORI_PRODUKSI.WAKTU_SELESAI, HISTORI_PRODUKSI.JUMLAH, HISTORI_PRODUKSI.XP, PETAK_SAWAH.JENIS_TANAMAN FROM (HISTORI_TANAMAN NATURAL JOIN HISTORI_PRODUKSI), BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH, PETAK_SAWAH WHERE HISTORI_TANAMAN.ID_BIBIT_TANAMAN = BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH.ID_BIBIT_TANAMAN AND BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH.ID_PETAK_SAWAH = PETAK_SAWAH.ID_ASET AND HISTORI_TANAMAN.EMAIL IN (SELECT PENGGUNA.EMAIL FROM PENGGUNA);""")
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
            cursor.execute("""SELECT HISTORI_TANAMAN.WAKTU_AWAL, HISTORI_PRODUKSI.WAKTU_SELESAI, HISTORI_PRODUKSI.JUMLAH, HISTORI_PRODUKSI.XP, PETAK_SAWAH.JENIS_TANAMAN FROM (HISTORI_TANAMAN NATURAL JOIN HISTORI_PRODUKSI), BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH, PETAK_SAWAH WHERE HISTORI_TANAMAN.ID_BIBIT_TANAMAN = BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH.ID_BIBIT_TANAMAN AND BIBIT_TANAMAN_DITANAM_DI_PETAK_SAWAH.ID_PETAK_SAWAH = PETAK_SAWAH.ID_ASET AND HISTORI_TANAMAN.EMAIL = %s;""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'historitanaman/readHistoriTanamanPengguna.html', {'result':result})
