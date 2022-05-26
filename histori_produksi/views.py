import email
from math import prod
from operator import truediv
from unittest import result
from django.shortcuts import redirect, render
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
    cursor.execute("SET search_path TO hidayb06")
    cursor.execute("SELECT * FROM PRODUK P WHERE P.ID IN (SELECT * FROM PRODUK_MAKANAN)")
    produk = cursor.fetchall()
    response = {}
    response['produk_makanan'] = []
    for i in range(len(produk)):
        response['produk_makanan'].append([
            produk[i][0], produk[i][1]
        ])
    if (request.method == 'POST'):
        if (request.POST['jumlah'] == ""):
            response['message'] = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'histori_produksi/produksiProdukMakanan.html', response)
        else:
            id_produk_makanan = request.POST['id_produk_makanan']
            jumlah_produksi = int(request.POST['jumlah'])
            xp = int(request.POST['xp'])
            now = datetime.now()
            dt_string = now.strftime("%Y/%m/%d %H%M%S")

            cursor.execute(""" SELECT P.ID_PRODUK, P.JUMLAH 
            FROM PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN P
            WHERE P.ID_PRODUK_MAKANAN = %s
            ORDER BY P.ID_PRODUK; """,[request.POST['id_produk_makanan']])
            bahan = cursor.fetchall()
            jumlah_dibutuhkan = list(i[1] for i in bahan)
            jumlah_produksi = request.POST['jumlah']
            total_bahan = []
            for i in jumlah_dibutuhkan:
                total_bahan.append(int(i)*jumlah_produksi)
            
            cursor.execute(""" SELECT L.ID_PRODUK, L.JUMLAH 
            FROM LUMBUNG_MEMILIKI_PRODUK L
            WHERE L.ID_PRODUK IN (SELECT P.ID_PRODUK 
            FROM PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN P
            WHERE P.ID_PRODUK_MAKANAN = %s) AND L.ID_LUMBUNG = %s
            ORDER BY L.ID_PRODUK""",[request.POST['id_produk_makanan'], email])
            jumlah = cursor.fetchall()
            jumlah_dimiliki = list(i[1] for i in jumlah)
            
            valid = True
            if (len(jumlah_dimiliki)<len(jumlah_dibutuhkan)):
                valid = False
            else:
                for i in range (len(jumlah_dimiliki)):
                    if (jumlah_dibutuhkan[i]>jumlah_dimiliki[i]):
                        valid = False
                        break

            if(valid):
                cursor.execute("INSERT INTO HISTORI_PRODUKSI VALUES (%s, %s, %s, %s, %s)", [email, dt_string, dt_string, request.POST['jumlah'],request.POST['xp']])
                cursor.execute("SELECT P.ID_ALAT_PRODUKSI FROM PRODUKSI P WHERE P.ID_PRODUK_MAKANAN = %s", [request.POST['id_produk_makanan']])
                result = cursor.fetchone()
                id_alat_produksi = result[0]
                cursor.execute("INSERT INTO HISTORI_PRODUKSI_MAKANAN VALUES (%s, %s, %s, %s)", [email, dt_string, id_alat_produksi, request.POST['id_produk_makanan']])
                return redirect ('/histori_produksi/historiprodukmakanan')
            else :        
                response['message'] = "Anda tidak memiliki bibit yang cukup, silahkan membeli bibit terlebih dahulu"
                return render(request, 'histori_produksi/produksiProdukMakanan.html', response)
    else:
        return render(request, 'histori_produksi/produksiProdukMakanan.html', response)