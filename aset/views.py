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
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetPengguna.html', {'result': result})
    elif (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT *
            FROM ASET;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)
        return render (request, 'aset/listAsetAdmin.html', {'result': result})

def buataset(request):
    return render (request, 'aset/buatAset.html')