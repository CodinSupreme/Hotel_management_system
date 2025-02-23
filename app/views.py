from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

User = Account()
# Create your views here.

#funtion loads the home page
def index(request):
    print(User.user)
    return render(request, 'index.HTML')

#function loads the Sign up page
def Register(request):
    if request.method == 'POST':
        if User.Register(f_name=request.POST['f_name'], l_name=request.POST['l_name'], email=request.POST['email'], id_no=request.POST['id'],contact=request.POST['contact'], gender=request.POST['gender'], password=request.POST['password']):
            return redirect('login')
        else: 
            
            return render(request, 'Register.HTML', {'message': {'msgbool': 1}})
    else:
        return render(request, 'Register.HTML', {'message': {'msgbool': 0}})

#function loads the login page
def Login(request):
    if request.method == 'POST':
        email=request.POST['email']

        if User.Auth(email=email, password=request.POST['password']):
            if Staff.objects.filter(email=email).exists():
                User.user = list(Staff.objects.filter(email=email).values())[0]['staff_id']
                return redirect('staff')
            else:
                User.user = list(Client.objects.filter(email=email).values())[0]['client_id']
                return redirect('client')
            
        else:
            return render(request, 'Login.HTML', {'message': {'msgbool': 1}})
    else:
        return render(request, 'Login.HTML', {'message': {'msgbool': 0}})

#function loads the staff page
def Staff_fun(request):
    staff = list(Staff.objects.filter(staff_id=User.user).values())[0]
    service = list(Service.objects.filter(service_id=User.user).values())
    return render(request, 'staff.html', {'staff':staff, 'services':service})

#function loads the client page
def Client_fun(request):
    client = list(Client.objects.filter(client_id=User.user).values())[0]
    return render(request, 'client.HTML', {'client': client})