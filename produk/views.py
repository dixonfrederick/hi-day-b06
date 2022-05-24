from calendar import c
from distutils.util import execute
from email import message
from unittest import result
from django.shortcuts import redirect, render
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
    cursor.execute("SET SEARCH_PATH TO public")
    role = request.session ['role']
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("""SELECT P.ID FROM PRODUK P
    WHERE P.ID NOT IN (SELECT ID_PRODUK FROM DETAIL_PESANAN) AND
    P.ID NOT IN (SELECT ID_PRODUK FROM LUMBUNG_MEMILIKI_PRODUK) AND
    P.ID NOT IN (SELECT ID_PRODUK FROM PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN) AND
    P.ID NOT IN (SELECT ID_PRODUK_MAKANAN FROM PRODUKSI) AND
    P.ID NOT IN (SELECT ID_PRODUK_HEWAN FROM HEWAN_MENGHASILKAN_PRODUK_HEWAN) AND
    P.ID NOT IN (SELECT ID_HASIL_PANEN FROM BIBIT_TANAMAN_MENGHASILKAN_HASIL_PANEN)""")
    deletable = cursor.fetchall()
    delete = []
    for i in range(len(deletable)):
        delete.append(deletable[i][0])
    if (role == "pengguna"):
        try:
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
        return render (request, 'produk/listProdukAdmin.html', {'result': result, 'delete':delete})

def buatProduk(request):
    cursor = connection.cursor()            
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    if (request.method == 'POST'):
        if (request.POST['nama'] == "" or request.POST['harga_jual'] == "" or request.POST['sifat_produk'] == ""):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'produk/buatProduk.html', {'message':message})
        else:
            if (request.POST['jenis_produk'] == 'hasil_panen'):
                cursor.execute("SELECT * FROM PRODUK P WHERE P.ID LIKE 'HP%' ORDER BY P.ID ASC")
                result = cursor.fetchall()
                if (len(result) == 0):
                    id = 'HP1'
                else :
                    last_id = (((result[-1])[0])[2:])
                    last_number = int(last_id) + 1
                    id = 'HP' + str(last_number)
                cursor.execute("INSERT INTO PRODUK VALUES (%s, %s, %s, %s)", [id, request.POST['nama'], request.POST['harga_jual'], request.POST['sifat_produk']])    
                cursor.execute("INSERT INTO HASIL_PANEN VALUES (%s)", [id])    
            elif (request.POST['jenis_produk'] == 'produk_hewan'):
                cursor.execute("SELECT * FROM PRODUK WHERE ID LIKE 'PH%' ORDER BY ID ASC")
                result = cursor.fetchall()
                if (len(result) == 0):
                    id = 'PH1'
                else :
                    last_id = (((result[-1])[0])[2:])
                    last_number = int(last_id) + 1
                    id = 'PH' + str(last_number)
                cursor.execute("INSERT INTO PRODUK VALUES (%s, %s, %s, %s)", [id, request.POST['nama'], request.POST['harga_jual'], request.POST['sifat_produk']])    
                cursor.execute("INSERT INTO PRODUK_HEWAN VALUES (%s)", [id])
            elif (request.POST['jenis_produk'] == 'produk_makanan'):
                cursor.execute("SELECT * FROM PRODUK WHERE ID LIKE 'PM%' ORDER BY ID ASC")
                result = cursor.fetchall()
                if (len(result) == 0):
                    id = 'PM1'
                else :
                    last_id = (((result[-1])[0])[2:])
                    last_number = int(last_id) + 1
                    id = 'PM' + str(last_number)
                cursor.execute("INSERT INTO PRODUK VALUES (%s, %s, %s, %s)", [id, request.POST['nama'], request.POST['harga_jual'], request.POST['sifat_produk']])    
                cursor.execute("INSERT INTO PRODUK_MAKANAN VALUES (%s)", [id])
        return redirect ('/produk/listproduk')
    return render (request, 'produk/buatProduk.html')

def updateProduk(request, id):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("""SELECT *,
        CASE 
        WHEN P.ID IN(SELECT PH.id_produk FROM PRODUK_HEWAN PH) THEN 'Produk Hewan'
        WHEN P.ID IN(SELECT HP.id_produk FROM HASIL_PANEN HP) THEN 'Hasil Panen'
        WHEN P.ID IN(SELECT PM.id_produk FROM PRODUK_MAKANAN PM) THEN 'Produk Makanan'
        END AS JENIS
        FROM PRODUK P 
        WHERE P.ID = %s;""", [id])
    result = cursor.fetchall()
    jenis = (result[0])[4]
    nama = (result[0])[1]
    if (request.method == 'POST'):
        if (request.POST['harga_jual'] == "" or request.POST['sifat_produk'] == ""):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'produk/updateProduk.html', {'message':message})
        else:
            cursor.execute("UPDATE PRODUK SET HARGA_JUAL = %s, SIFAT_PRODUK = %s WHERE PRODUK.ID = %s", [request.POST['harga_jual'], request.POST['sifat_produk'], id])
            return redirect ('/produk/listproduk')
    else:
        return render (request, 'produk/updateProduk.html', {'jenis':jenis, 'nama':nama})

def deleteProduk(request, id):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("DELETE FROM PRODUK P WHERE P.ID = %s", [id])
    return redirect ('/produk/listproduk')

def listProduksi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("""SELECT * FROM PRODUKSI P
    WHERE (P.ID_ALAT_PRODUKSI, P.ID_PRODUK_MAKANAN) NOT IN (SELECT ID_ALAT_PRODUKSI, ID_PRODUK_MAKANAN FROM HISTORI_PRODUKSI_MAKANAN)""")
    deletable = namedtuplefetchall(cursor)
    if (role == "pengguna"):
        try:
            cursor.execute("""SELECT P.ID_ALAT_PRODUKSI, P.ID_PRODUK_MAKANAN, PR.NAMA AS PRODUK_MAKANAN, A.NAMA AS ALAT_PRODUKSI, EXTRACT (MINUTE FROM P.DURASI) AS DURASI, P.JUMLAH_UNIT_HASIL
            FROM PRODUKSI P, PRODUK PR, ASET A
            WHERE P.ID_ALAT_PRODUKSI = A.ID AND P.ID_PRODUK_MAKANAN = PR.ID;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'produk/listProduksiPengguna.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("""SELECT P.ID_ALAT_PRODUKSI, P.ID_PRODUK_MAKANAN, PR.NAMA AS PRODUK_MAKANAN, A.NAMA AS ALAT_PRODUKSI, EXTRACT (MINUTE FROM P.DURASI) AS DURASI, P.JUMLAH_UNIT_HASIL
            FROM PRODUKSI P, PRODUK PR, ASET A
            WHERE P.ID_ALAT_PRODUKSI = A.ID AND P.ID_PRODUK_MAKANAN = PR.ID;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'produk/listProduksiAdmin.html', {'result': result, 'deletable':deletable})

def detailProduksi(request, id_alat_produksi, id_produk_makanan):
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute("SET SEARCH_PATH TO hidayb06")
        cursor.execute("""SELECT PR.NAMA AS PRODUK_MAKANAN, A.NAMA AS ALAT_PRODUKSI, EXTRACT (MINUTE FROM P.DURASI) AS DURASI, P.JUMLAH_UNIT_HASIL
        FROM PRODUKSI P, PRODUK PR, ASET A
        WHERE P.ID_ALAT_PRODUKSI = A.ID AND P.ID_PRODUK_MAKANAN = PR.ID AND P.ID_ALAT_PRODUKSI = %s AND P.ID_PRODUK_MAKANAN = %s;""", [id_alat_produksi, id_produk_makanan])
        result = namedtuplefetchall(cursor)
        cursor.execute("""SELECT P.NAMA AS BAHAN, PD.JUMLAH 
        FROM PRODUK P, PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN PD
        WHERE P.ID = PD.ID_PRODUK AND PD.ID_PRODUK_MAKANAN = %s""", [id_produk_makanan])
        bahan = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
    return render(request, 'produk/detailProduksi.html', {'result': result, 'bahan':bahan})

def buatProduksi(request):
    response = {}
    response['produk_makanan'] = []
    response['alat_produksi'] = []
    cursor = connection.cursor()
    # cursor.execute("SET search_path TO public")
    # email = request.session ['email']
    cursor.execute("SET search_path TO hidayb06")
    cursor.execute("SELECT * FROM PRODUK P WHERE P.ID IN (SELECT * FROM PRODUK_MAKANAN)")
    produk = cursor.fetchall()
    for i in range(len(produk)):
        response['produk_makanan'].append([
            produk[i][0], produk[i][1]
        ])

    cursor.execute("SELECT * FROM ASET A WHERE A.ID IN (SELECT ID_ASET FROM ALAT_PRODUKSI)")
    alat = cursor.fetchall()
    for i in range(len(alat)):
        response['alat_produksi'].append([
            alat[i][0], alat[i][1]
        ])
    return render (request, 'produk/buatProduksi.html')

def updateProduksi(request, id_alat_produksi, id_produk_makanan):
    cursor = connection.cursor()
    result = []
    try:
        cursor.execute("SET SEARCH_PATH TO hidayb06")
        cursor.execute("""SELECT PR.NAMA AS PRODUK_MAKANAN, A.NAMA AS ALAT_PRODUKSI, EXTRACT (MINUTE FROM P.DURASI) AS DURASI, P.JUMLAH_UNIT_HASIL
        FROM PRODUKSI P, PRODUK PR, ASET A
        WHERE P.ID_ALAT_PRODUKSI = A.ID AND P.ID_PRODUK_MAKANAN = PR.ID AND P.ID_ALAT_PRODUKSI = %s AND P.ID_PRODUK_MAKANAN = %s;""", [id_alat_produksi, id_produk_makanan])
        result = namedtuplefetchall(cursor)
        cursor.execute("""SELECT P.NAMA AS BAHAN, PD.JUMLAH 
        FROM PRODUK P, PRODUK_DIBUTUHKAN_OLEH_PRODUK_MAKANAN PD
        WHERE P.ID = PD.ID_PRODUK AND PD.ID_PRODUK_MAKANAN = %s""", [id_produk_makanan])
        bahan = namedtuplefetchall(cursor)
    except Exception as e:
        print(e)
    if (request.method == 'POST'):
        if (request.POST['durasi'] == "" or request.POST['jumlah'] == ""):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'produk/updateProduksi.html', {'result': result, 'bahan':bahan, 'message':message})
        else:
            minute = request.POST['durasi']
            if (len(minute) == 1):
                minute = "0"+minute
            durasi = "00:" + minute + ":00"
            cursor.execute("UPDATE PRODUKSI P SET DURASI = %s, JUMLAH_UNIT_HASIL = %s WHERE P.ID_PRODUK_MAKANAN = %s AND P.ID_ALAT_PRODUKSI = %s", [durasi, request.POST['jumlah'], id_produk_makanan, id_alat_produksi])
            return redirect ('/produk/listproduksi')
    else:
        return render(request, 'produk/updateProduksi.html', {'result': result, 'bahan':bahan})
 

def deleteProduksi(request, id_alat_produksi, id_produk_makanan):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    cursor.execute("DELETE FROM PRODUKSI P WHERE P.ID_ALAT_PRODUKSI = %s AND P.ID_PRODUK_MAKANAN = %s", [id_alat_produksi, id_produk_makanan])
    return redirect ('/produk/listproduksi')
