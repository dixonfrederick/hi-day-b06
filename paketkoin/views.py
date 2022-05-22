import email
from collections import namedtuple
import imp
import re
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError, InterfaceError
from .forms import *
from .forms2 import *

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def createpaketkoinadmin(request):
    form = CreatePaketKoinAdminForm(request.POST or None)
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    if (form.is_valid() and request.method == 'POST'):
        jumlah_koin = form.cleaned_data['jumlah_koin']
        harga = form.cleaned_data['harga']
        if ((jumlah_koin is not None) and (harga is not None)):
            try:
                cursor.execute("INSERT INTO PAKET_KOIN (jumlah_koin,harga) VALUES (%d,%d)", [jumlah_koin,harga])
                cursor.execute("SET SEARCH_PATH TO public")
                return redirect("/readpaketkoinadmin")
            except Exception as error:
                print(error)
        else:
            message = "Masih ada yang kosong"
            return render(request, 'paketkoin/createPaketKoinAdmin.html', {'message':message})
    else:
        return render(request, 'paketkoin/createPaketKoinAdmin.html', {'form':form})

def deletepaketkoinadmin(request):
    
    context = {}
    return render(request, 'paketkoin/deletePaketKoinAdmin.html', context)

def readpaketkoinadmin(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "admin"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT JUMLAH_KOIN, HARGA FROM PAKET_KOIN;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'paketkoin/readPaketKoinAdmin.html', {'result':result})

def readpaketkoinpengguna(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    role = request.session ['role']
    userEmail = request.session ['email']
    if (role == "pengguna"):
        try:
            cursor.execute("SET SEARCH_PATH TO hidayb06")
            cursor.execute("""SELECT JUMLAH_KOIN, HARGA FROM PAKET_KOIN;""")
            result = namedtuplefetchall(cursor)
        except Exception as e:
            print(e)

        return render(request, 'paketkoin/readPaketKoinPengguna.html', {'result':result})

def updatepaketkoinadmin(request):

    form = UpdatePaketKoinAdminForm(request.POST or None)
    context = {'form':form}
    return render(request, 'paketkoin/updatePaketKoinAdmin.html', context)
