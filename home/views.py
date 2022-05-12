from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError, InterfaceError
from django.db import connections
from forms import *
from forms2 import *
from forms3 import *

# Create your views here.
role = ""
def index(request):
    if role == "pengguna":
        return render(request, 'home/baseAdmin.html')
    elif role == "admin":
        return render(request, 'home/basePengguna.html')

def login(request):
    MyForm = CreateUserForm3(request.POST)
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
        return render(request, 'home/login.html', {'form' : MyForm})

def home(request):
    cursor = connection.cursor()
    cursor.execute("SET search_path TO public")
    if request.session.has_key('email'):
        role = request.session ['role']
        return render (request, 'home/home.html', {'role': role})
    else:
        return render(request, 'home/login.html')

def logout(request):
    if 'user_email' not in request.session or 'user_role' not in request.session:
        return redirect('home:login')
    request.session.flush()
    return redirect('home:login')

def registeradmin(request):
    form = CreateUserForm(request.POST or None)
    context = {'form':form}
    return render(request, 'home/registerAdmin.html', context)

def registerpengguna(request):
    form = CreateUserForm2(request.POST or None)
    context = {'form':form}
    return render(request, 'home/registerPengguna.html', context)