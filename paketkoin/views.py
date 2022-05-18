import email
from collections import namedtuple
import imp
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
    context = {'form':form}
    return render(request, 'paketkoin/createPaketKoinAdmin.html',context)

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
