from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listkoleksi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        return render (request, 'koleksiaset/listKoleksiPengguna.html')
    elif (role == "admin"):
        return render (request, 'koleksiaset/listKoleksiAdmin.html')

def listkoleksi_dekorasi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, DEKORASI
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND DEKORASI.ID_ASET = ID AND KOLEKSI_ASET.EMAIL = %s""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiPengguna_Dekorasi.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, DEKORASI
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND DEKORASI.ID_ASET = ID""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiAdmin_Dekorasi.html', {'result': result})

def listkoleksi_bibittanaman(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, BIBIT_TANAMAN
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND BIBIT_TANAMAN.ID_ASET = ID AND KOLEKSI_ASET.EMAIL = %s""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiPengguna_BibitTanaman.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, BIBIT_TANAMAN
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND BIBIT_TANAMAN.ID_ASET = ID""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiAdmin_BibitTanaman.html', {'result': result})

def listkoleksi_kandang(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, KANDANG
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND KANDANG.ID_ASET = ID AND KOLEKSI_ASET.EMAIL = %s""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiPengguna_Kandang.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, KANDANG
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND KANDANG.ID_ASET = ID""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiAdmin_Kandang.html', {'result': result})

def listkoleksi_hewan(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, HEWAN
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND HEWAN.ID_ASET = ID AND KOLEKSI_ASET.EMAIL = %s""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiPengguna_Hewan.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, HEWAN
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND HEWAN.ID_ASET = ID""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiAdmin_Hewan.html', {'result': result})

def listkoleksi_alatproduksi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, ALAT_PRODUKSI
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND ALAT_PRODUKSI.ID_ASET = ID AND KOLEKSI_ASET.EMAIL = %s""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiPengguna_AlatProduksi.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, ALAT_PRODUKSI
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND ALAT_PRODUKSI.ID_ASET = ID""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiAdmin_AlatProduksi.html', {'result': result})

def listkoleksi_petaksawah(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, PETAK_SAWAH
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND PETAK_SAWAH.ID_ASET = ID AND KOLEKSI_ASET.EMAIL = %s""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiPengguna_PetakSawah.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT ID_KOLEKSI_ASET, NAMA, MINIMUM_LEVEL, HARGA_BELI, JUMLAH
            FROM KOLEKSI_ASET, KOLEKSI_ASET_MEMILIKI_ASET, ASET, PETAK_SAWAH
            WHERE ID_KOLEKSI_ASET = EMAIL AND KOLEKSI_ASET_MEMILIKI_ASET.ID_ASET = ID
            AND PETAK_SAWAH.ID_ASET = ID""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'koleksiaset/listKoleksiAdmin_PetakSawah.html', {'result': result})
