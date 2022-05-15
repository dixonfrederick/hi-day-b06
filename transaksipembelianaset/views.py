from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def listtransaksi(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT TRANSAKSI_PEMBELIAN.EMAIL, WAKTU, NAMA, JUMLAH, HARGA_BELI * JUMLAH AS TOTAL_HARGA
            FROM ASET, KOLEKSI_ASET, TRANSAKSI_PEMBELIAN
            WHERE KOLEKSI_ASET.EMAIL = TRANSAKSI_PEMBELIAN.EMAIL AND ID_ASET = ID AND KOLEKSI_ASET.EMAIL = %s;""", [userEmail])
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'transaksipembelianaset/listTransaksiPengguna.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT TRANSAKSI_PEMBELIAN.EMAIL, WAKTU, NAMA, JUMLAH, HARGA_BELI * JUMLAH AS TOTAL_HARGA
            FROM ASET, KOLEKSI_ASET, TRANSAKSI_PEMBELIAN
            WHERE KOLEKSI_ASET.EMAIL = TRANSAKSI_PEMBELIAN.EMAIL AND ID_ASET = ID;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'transaksipembelianaset/listTransaksiAdmin.html', {'result': result})

def buattransaksi(request):
    return render (request, 'transaksipembelianaset/buattransaksi.html')