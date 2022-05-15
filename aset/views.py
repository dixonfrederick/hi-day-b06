from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def createasetadmin(request):
    return render (request, 'aset/createasetadmin.html')

def readasetadmin(request):
    return render (request, 'aset/readasetadmin.html')

def updateasetadmin(request):
    return render (request, 'aset/updateasetadmin.html')

def deleteasetadmin(request):
    return render (request, 'aset/deleteasetadmin.html')

def readasetpengguna(request):
    return render (request, 'aset/readasetpengguna.html')