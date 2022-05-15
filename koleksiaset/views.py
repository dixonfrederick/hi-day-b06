from django.shortcuts import render
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db import connection
from collections import namedtuple

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def readkoleksiasetadmin(request):
    return render (request, 'aset/readkoleksiasetadmin.html')

def readkoleksiasetpengguna(request):
    return render (request, 'aset/readkoleksiasetpengguna.html')