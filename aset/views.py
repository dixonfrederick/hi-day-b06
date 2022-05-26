from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listaset(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        return render (request, 'aset/listAsetPengguna.html')
    elif (role == "admin"):
        return render (request, 'aset/listAsetAdmin.html')

def listaset_dekorasi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, DEKORASI
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetPengguna_Dekorasi.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, DEKORASI
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetAdmin_Dekorasi.html', {'result': result})

def listaset_bibittanaman(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, BIBIT_TANAMAN
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetPengguna_BibitTanaman.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, BIBIT_TANAMAN
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetAdmin_BibitTanaman.html', {'result': result})

def listaset_kandang(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, KANDANG
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetPengguna_Kandang.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, KANDANG
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetAdmin_Kandang.html', {'result': result})

def listaset_hewan(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, HEWAN
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetPengguna_Hewan.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, HEWAN
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetAdmin_Hewan.html', {'result': result})

def listaset_alatproduksi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, ALAT_PRODUKSI
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetPengguna_AlatProduksi.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, ALAT_PRODUKSI
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetAdmin_AlatProduksi.html', {'result': result})

def listaset_petaksawah(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, PETAK_SAWAH
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetPengguna_PetakSawah.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET, PETAK_SAWAH
            WHERE ID = ID_ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetAdmin_PetakSawah.html', {'result': result})

def buataset(request):
    return render (request, 'aset/buatAset.html')