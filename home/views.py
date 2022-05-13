import email
import imp
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from collections import namedtuple
from django.db.utils import IntegrityError, InterfaceError

# Create your views here.
def namedtuplefetchall(cursor):
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def home(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    if request.session.has_key('email'):
        role = request.session ['role']
        email = request.session ['email']
        if (role == "pengguna"):
            try:
                cursor.execute("SET SEARCH_PATH TO hidayb06")
                cursor.execute("SELECT * FROM pengguna WHERE email = %s", [email])
                result = namedtuplefetchall(cursor)
            except Exception as e:
                print(e)
            return render (request, 'home/homePengguna.html', {'result': result})
        elif (role == "admin"):
            try:
                cursor.execute("SET SEARCH_PATH TO hidayb06")
                cursor.execute("SELECT * FROM admin WHERE email = %s", [email])
                result = namedtuplefetchall(cursor)
            except Exception as e:
                print(e)
            return render (request, 'home/homeAdmin.html', {'result': result})
    else:
        return redirect('login_register')

def logout(request):
    try:
        del request.session['email']
        del request.session['role']
    except:
        pass
    return redirect('/login_register/login')

