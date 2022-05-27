from django.shortcuts import redirect, render
from django.db import connection
from collections import namedtuple

# Create your views here.
def readlumbung(request):
    if request.session.get("role", None) == None:
        return redirect("/authentication/user_login")
    response = {}
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06;")
    if request.session.get("role") == 'admin':
        cursor.execute("""SELECT id_lumbung, id_produk, nama, harga_jual, sifat_produk, jumlah
                        FROM LUMBUNG_MEMILIKI_PRODUK LEFT OUTER JOIN PRODUK ON id_produk = id
                        WHERE id_produk in (
                        SELECT id_produk FROM HASIL_PANEN);""")
        response['hasil_panen'] = cursor.fetchall()
        cursor.execute("""SELECT id_lumbung, id_produk, nama, harga_jual, sifat_produk, jumlah
                        FROM LUMBUNG_MEMILIKI_PRODUK LEFT OUTER JOIN PRODUK ON id_produk = id
                        WHERE id_produk in (
                        SELECT id_produk FROM PRODUK_HEWAN);""")
        response['produk_hewan'] = cursor.fetchall()
        cursor.execute("""SELECT id_lumbung, id_produk, nama, harga_jual, sifat_produk, jumlah
                        FROM LUMBUNG_MEMILIKI_PRODUK LEFT OUTER JOIN PRODUK ON id_produk = id
                        WHERE id_produk in (
                        SELECT id_produk FROM PRODUK_MAKANAN);""")
        response['produk_makanan'] = cursor.fetchall()
        return render(request, 'lumbung/readLumbungAdmin.html', response)

    else:
        cursor.execute("""SELECT id_produk, nama, harga_jual, sifat_produk, jumlah
                        FROM LUMBUNG_MEMILIKI_PRODUK LEFT OUTER JOIN PRODUK ON id_produk = id
                        WHERE id_lumbung = %s AND
                        id_produk in (
                        SELECT id_produk FROM HASIL_PANEN);""", [request.session.get('email')])
        response['hasil_panen'] = cursor.fetchall()
        cursor.execute("""SELECT id_produk, nama, harga_jual, sifat_produk, jumlah
                        FROM LUMBUNG_MEMILIKI_PRODUK LEFT OUTER JOIN PRODUK ON id_produk = id
                        WHERE id_lumbung = %s AND
                        id_produk in (
                        SELECT id_produk FROM PRODUK_HEWAN);""", [request.session.get('email')])
        response['produk_hewan'] = cursor.fetchall()
        cursor.execute("""SELECT id_produk, nama, harga_jual, sifat_produk, jumlah
                        FROM LUMBUNG_MEMILIKI_PRODUK LEFT OUTER JOIN PRODUK ON id_produk = id
                        WHERE id_lumbung = %s AND
                        id_produk in (
                        SELECT id_produk FROM PRODUK_MAKANAN);""", [request.session.get('email')])
        response['produk_makanan'] = cursor.fetchall()
        cursor.execute("""SELECT LEVEL, round((total/kapasitas_maksimal::float)*100)
                        FROM LUMBUNG WHERE email = %s;""", [request.session.get('email')])
        result = cursor.fetchall()
        if len(result) != 0:
            lumbung = result[0]
            response['level'] = lumbung[0]
            response['kapasitas'] = lumbung[1]
        else:
            response['level'] = '-'
            response['kapasitas'] = '-'
        return render(request, 'lumbung/readLumbungPengguna.html', response)

