from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import IntegrityError, InterfaceError
from django.db import connections

# Create your views here.
peran = ""
def index(request):
    if peran == "pengguna":
        return render(request, 'home/baseAdmin.html')
    elif peran == "admin":
        return render(request, 'home/basePengguna.html')

def login(request):
    context = {}
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            with connection.cursor() as c:
                c.execute("SET search_path to hiday;")
                c.execute(f"select * from admin where email = '{email}' and password = '{password}';")
                admin = c.fetchone()
                c.execute(f"select * from pengguna where email = '{email}' and password = '{password}';")
                pengguna = c.fetchone()
                if admin != None or pengguna != None:
                    c.execute(f"select * from admin where email = '{email}';")
                    admin = c.fetchone()
                    c.execute(f"select * from pengguna where email = '{email}';")
                    pengguna = c.fetchone()
                    if admin:
                        peran = "admin"
                    if pengguna:
                        peran = "pengguna"
                    
                    request.session["user_email"] = email
                    request.session["user_role"] = peran
                else:
                    context["error"] = "Wrong Email or Password"
                    return render(request, 'registration/login.html', context)
        except:
            context["error"] = "Error fetching data"
            return render(request, 'registration/login.html', context)
        return redirect("main:home")
    return render(request, 'registration/login.html')

def logout(request):
    if 'user_email' not in request.session or 'user_role' not in request.session:
        return redirect('main:login')
    request.session.flush()
    return redirect('main:login')

def registeradmin(request):
    form = CreateUserForm(request.POST or None)
    context = {'form':form}
    return render(request, 'home/registeradmin.html', context)

def registerpengguna(request):
    form = CreateUserForm2(request.POST or None)
    context = {'form':form}
    return render(request, 'home/registerpengguna.html', context)
