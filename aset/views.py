from django.http import QueryDict
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

def buatasetdekorasi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SET search_path TO hidayb06")
    if (request.method == 'POST'):
        res = request.POST
        id = res.get('id') 
        nama = res.get('nama')
        minimum_level = res.get('minimum_level')
        harga_beli = res.get('harga_beli')
        harga_jual = res.get('harga_jual')
        cursor.execute("""SELECT max(cast(substring(id,3) as integer)) 
        FROM ASET 
        WHERE id LIKE 'DK%'"""
        )
        result = namedtuplefetchall(cursor);
        if (result[0].max is None):
            id = 'DK0'
        else :
            resinc = result[0].max + 1
            id = 'DK' + str(resinc)
        cursor.execute("""INSERT INTO ASET
        VALUES (%s, %s, %s, %s)""", [id, nama, minimum_level, harga_beli])
        cursor.execute("""INSERT INTO DEKORASI
        VALUES (%s, %s)""", [id, harga_jual])
    return render (request, 'aset/buatAsetDekorasi.html')

def buatasetbibittanaman(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SET search_path TO hidayb06")
    if (request.method == 'POST'):
        res = request.POST
        id = res.get('id') 
        nama = res.get('nama')
        minimum_level = res.get('minimum_level')
        harga_beli = res.get('harga_beli')
        durasi_panen = res.get('durasi_panen')
        cursor.execute("""SELECT max(cast(substring(id,3) as integer)) 
        FROM ASET 
        WHERE id LIKE 'BT%'"""
        )
        result = namedtuplefetchall(cursor);
        if (result[0].max is None):
            id = 'BT0'
        else :
            resinc = result[0].max + 1
            id = 'BT' + str(resinc)
        cursor.execute("""INSERT INTO ASET
        VALUES (%s, %s, %s, %s)""", [id, nama, minimum_level, harga_beli])
        cursor.execute("""INSERT INTO BIBIT_TANAMAN
        VALUES (%s, %s)""", [id, durasi_panen])
    return render (request, 'aset/buatAsetBibitTanaman.html')

def buatasetkandang(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SET search_path TO hidayb06")
    if (request.method == 'POST'):
        res = request.POST
        id = res.get('id') 
        nama = res.get('nama')
        minimum_level = res.get('minimum_level')
        harga_beli = res.get('harga_beli')
        kapasitas_maks = res.get('kapasitas_maks')
        jenis_hewan = res.get('jenis_hewan')
        cursor.execute("""SELECT max(cast(substring(id,3) as integer)) 
        FROM ASET 
        WHERE id LIKE 'KD%'"""
        )
        result = namedtuplefetchall(cursor);
        if (result[0].max is None):
            id = 'KD0'
        else :
            resinc = result[0].max + 1
            id = 'KD' + str(resinc)
        cursor.execute("""INSERT INTO ASET
        VALUES (%s, %s, %s, %s)""", [id, nama, minimum_level, harga_beli])
        cursor.execute("""INSERT INTO KANDANG
        VALUES (%s, %s, %s)""", [id, kapasitas_maks, jenis_hewan])
    return render (request, 'aset/buatAsetKandang.html')

def buatasethewan(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SET search_path TO hidayb06")
    if (request.method == 'POST'):
        res = request.POST
        id = res.get('id') 
        nama = res.get('nama')
        minimum_level = res.get('minimum_level')
        harga_beli = res.get('harga_beli')
        durasi_produksi = res.get('durasi_produksi')
        id_kandang = res.get('id_kandang')
        cursor.execute("""SELECT max(cast(substring(id,3) as integer)) 
        FROM ASET 
        WHERE id LIKE 'HW%'"""
        )
        result = namedtuplefetchall(cursor);
        if (result[0].max is None):
            id = 'HW0'
        else :
            resinc = result[0].max + 1
            id = 'HW' + str(resinc)
        cursor.execute("""INSERT INTO ASET
        VALUES (%s, %s, %s, %s)""", [id, nama, minimum_level, harga_beli])
        cursor.execute("""INSERT INTO HEWAN
        VALUES (%s, %s, %s)""", [id, durasi_produksi, id_kandang])
    return render (request, 'aset/buatAsetHewan.html')

def buatasetalatproduksi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SET search_path TO hidayb06")
    if (request.method == 'POST'):
        res = request.POST
        id = res.get('id') 
        nama = res.get('nama')
        minimum_level = res.get('minimum_level')
        harga_beli = res.get('harga_beli')
        kapasitas_maks = res.get('kapasitas_maks')
        cursor.execute("""SELECT max(cast(substring(id,3) as integer)) 
        FROM ASET 
        WHERE id LIKE 'AP%'"""
        )
        result = namedtuplefetchall(cursor);
        if (result[0].max is None):
            id = 'AP0'
        else :
            resinc = result[0].max + 1
            id = 'AP' + str(resinc)
        cursor.execute("""INSERT INTO ASET
        VALUES (%s, %s, %s, %s)""", [id, nama, minimum_level, harga_beli])
        cursor.execute("""INSERT INTO ALAT_PRODUKSI
        VALUES (%s, %s)""", [id, kapasitas_maks])
    return render (request, 'aset/buatAsetAlatProduksi.html')

def buatasetpetaksawah(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    cursor.execute("SET search_path TO hidayb06")
    if (request.method == 'POST'):
        res = request.POST
        id = res.get('id') 
        nama = res.get('nama')
        minimum_level = res.get('minimum_level')
        harga_beli = res.get('harga_beli')
        jenis_tanaman = res.get('jenis_tanaman')
        cursor.execute("""SELECT max(cast(substring(id,3) as integer)) 
        FROM ASET 
        WHERE id LIKE 'PS%'"""
        )
        result = namedtuplefetchall(cursor);
        if (result[0].max is None):
            id = 'PS0'
        else :
            resinc = result[0].max + 1
            id = 'PS' + str(resinc)
        cursor.execute("""INSERT INTO ASET
        VALUES (%s, %s, %s, %s)""", [id, nama, minimum_level, harga_beli])
        cursor.execute("""INSERT INTO PETAK_SAWAH
        VALUES (%s, %s)""", [id, jenis_tanaman])
    return render (request, 'aset/buatAsetPetakSawah.html')