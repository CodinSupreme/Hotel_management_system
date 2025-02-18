from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

User = Account()
# Create your views here.
def index(request):
    print(User.user)
    return render(request, 'index.HTML')

def Register(request):
    if request.method == 'POST':
        if User.Register(f_name=request.POST['f_name'], l_name=request.POST['l_name'], email=request.POST['email'], id_no=request.POST['id'],contact=request.POST['contact'], gender=request.POST['gender'], password=request.POST['password']):
            return redirect('login')
        else: 
            print("error")
            return render(request, 'Register.HTML')
    else:
        return render(request, 'Register.HTML')

def Login(request):
    if request.method == 'POST':
        if User.Auth(email=request.POST['email'], password=request.POST['password']):
            User.user=str(request.POST['email'])
            return redirect('index')
        else:
            print('error')
            return render(request, 'Login.HTML')
    else:
        return render(request, 'Login.HTML')

def Staff(request):
    pass

def Client(request):
    pass