from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listProduk(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *,
            CASE 
            WHEN P.ID IN(SELECT PH.id_produk FROM PRODUK_HEWAN PH) THEN 'Produk Hewan'
            WHEN P.ID IN(SELECT HP.id_produk FROM HASIL_PANEN HP) THEN 'Hasil Panen'
            WHEN P.ID IN(SELECT PM.id_produk FROM PRODUK_MAKANAN PM) THEN 'Produk Makanan'
            END AS JENIS
            FROM PRODUK P;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'produk/listProdukPengguna.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *,
            CASE 
            WHEN P.ID IN(SELECT PH.id_produk FROM PRODUK_HEWAN PH) THEN 'Produk Hewan'
            WHEN P.ID IN(SELECT HP.id_produk FROM HASIL_PANEN HP) THEN 'Hasil Panen'
            WHEN P.ID IN(SELECT PM.id_produk FROM PRODUK_MAKANAN PM) THEN 'Produk Makanan'
            END AS JENIS
            FROM PRODUK P;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'produk/listProdukAdmin.html', {'result': result})