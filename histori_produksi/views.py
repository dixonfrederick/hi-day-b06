import email
from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple
from datetime import datetime

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def historiProdukMakanan(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    email = request.session ['email']
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06;")
            cursor.execute("""SELECT HPM.EMAIL, HPM.WAKTU_AWAL, HP.WAKTU_SELESAI, HP.JUMLAH, HP.XP, P.NAMA AS NAMA_PRODUK, A.NAMA AS NAMA_ASET
            FROM HISTORI_PRODUKSI_MAKANAN HPM, HISTORI_PRODUKSI HP, PRODUK P, ASET A
            WHERE HPM.EMAIL = HP.EMAIL AND HPM.EMAIL = %s AND HPM.WAKTU_AWAL = HP.WAKTU_AWAL AND HPM.ID_ALAT_PRODUKSI = A.ID AND HPM.ID_PRODUK_MAKANAN = P.ID;""", [email])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'histori_produksi/historiProdukMakananPengguna.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06;")
            cursor.execute("""SELECT HPM.EMAIL, HPM.WAKTU_AWAL, HP.WAKTU_SELESAI, HP.JUMLAH, HP.XP, P.NAMA AS NAMA_PRODUK, A.NAMA AS NAMA_ASET
            FROM HISTORI_PRODUKSI_MAKANAN HPM, HISTORI_PRODUKSI HP, PRODUK P, ASET A
            WHERE HPM.EMAIL = HP.EMAIL AND HPM.WAKTU_AWAL = HP.WAKTU_AWAL AND HPM.ID_ALAT_PRODUKSI = A.ID AND HPM.ID_PRODUK_MAKANAN = P.ID;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'histori_produksi/historiProdukMakananAdmin.html', {'result': result})    

def produksiProdukMakanan(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    email = request.session ['email']
    cursor.execute("SET search_path TO public")
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%d %H%M%S")
    if (request.method == 'POST'):
        if (request.POST['jumlah'] == ""):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'histori_produksi/produksiProdukMakanan.html', {'message':message})
        else:        
            cursor.execute("INSERT INTO HISTORI_PRODUKSI_MAKANAN VALUES")
    else:
        return render(request, 'histori_produksi/produksiProdukMakanan.html')