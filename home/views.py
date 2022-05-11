from django.shortcuts import render
from .forms import CreateUserForm
from .forms2 import CreateUserForm2

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def registeradmin(request):
    form = CreateUserForm(request.POST or None)
    context = {'form':form}
    return render(request, 'home/registeradmin.html', context)

def registerpengguna(request):
    form = CreateUserForm2(request.POST or None)
    context = {'form':form}
    return render(request, 'home/registerpengguna.html', context)

def login(request):
    form = CreateUserForm(request.POST or None)
    context = {'form':form}
    return render(request, 'home/login.html', context)
