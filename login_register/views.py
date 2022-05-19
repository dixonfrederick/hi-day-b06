from django.shortcuts import render, redirect
from django.db import connection
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.db.utils import IntegrityError, InterfaceError
from .forms import *
from .forms2 import *
from .forms3 import *
from .loginForms import *

# Create your views here.
def login(request):
    MyForm = LoginForm(request.POST)
    cursor = connection.cursor();            
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    # Form submission
    if (MyForm.is_valid() and request.method == 'POST'):
        
        # Define login form
        email = MyForm.cleaned_data['email']
        password = MyForm.cleaned_data['password']
        cursor.execute("SELECT email FROM akun WHERE email = %s", [email]) 
        result = cursor.fetchone()
        try :
            if(result == None): 
                return HttpResponseNotFound("The user does not exist")
                
            if(result is not None):
                cursor.execute("SELECT email from admin WHERE email = %s",[email])
                admin = cursor.fetchone()

                cursor.execute("SELECT email from pengguna WHERE email = %s",[email])
                pengguna = cursor.fetchone()
                
                #Assignment untuk mengetahui role user
                if(pengguna is not None):
                    role = "pengguna"
                    cursor.execute("SELECT email, password FROM pengguna WHERE email = %s AND password = %s", [email,password])
                    verif_akun = cursor.fetchone()
                elif (admin is not None):
                    role = "admin"
                    cursor.execute("SELECT email, password FROM admin WHERE email = %s AND password = %s", [email,password])
                    verif_akun = cursor.fetchone()
                if (verif_akun is not None):
                    cursor.execute("SET SEARCH_PATH TO public")
                    request.session['email'] = email
                    request.session['role'] = role
                    return redirect ("/home")
        except Exception as e:
            print(e)
            cursor.close()
        return redirect ("/login")

    else:
        cursor.execute("SET search_path TO public")
        return render(request, 'login_register/login.html', {'form' : MyForm})

def registeradmin(request):
    myForm = RegisterAdminForm(request.POST)
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    if (myForm.is_valid() and request.method == 'POST'):
        role = "admin"
        email = myForm.cleaned_data['email']
        password = myForm.cleaned_data['password']
        cursor.execute("SELECT EMAIL FROM ADMIN WHERE email = %s", [email]) 
        result = cursor.fetchone()
        if(result == None):
            try:
                cursor.execute("INSERT INTO AKUN VALUES (%s)", [email])
                cursor.execute("INSERT INTO ADMIN (email,password) VALUES (%s,%s)", [email,password])
                cursor.execute("SET SEARCH_PATH TO public")
                request.session['email'] = email
                request.session['role'] = role
                return redirect ("/home")
            except Exception as error:
                print(error)
        else:
                message = "User already exist"
                return render(request, 'login_register/registerAdmin.html', {'message':message})
    else :
        return render (request, 'login_register/registerAdmin.html', {'form':myForm})

def registerpengguna(request):
    myForm = RegisterPenggunaForm(request.POST)
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO hidayb06")
    if (myForm.is_valid() and request.method == 'POST'):
        role = "pengguna"
        email = myForm.cleaned_data['email']
        password = myForm.cleaned_data['password']
        nama_area_pertanian = myForm.cleaned_data['nama_area_pertanian']
        cursor.execute("SELECT EMAIL FROM PENGGUNA WHERE email = %s", [email]) 
        result = cursor.fetchone()
        if(result == None):
            try:
                cursor.execute("INSERT INTO AKUN VALUES (%s)", [email])
                cursor.execute("INSERT INTO PENGGUNA (email,password,nama_area_pertanian) VALUES (%s,%s,%s)", [email, password, nama_area_pertanian])
                cursor.execute("SET SEARCH_PATH TO public")
                request.session['email'] = email
                request.session['role'] = role
                return redirect ("/home")
            except Exception as error:
                print(error)
        else:
                message = "User already exist"
                return render(request, 'login_register/registerPengguna.html', {'message':message})
    else :
        return render (request, 'login_register/registerPengguna.html', {'form':myForm})