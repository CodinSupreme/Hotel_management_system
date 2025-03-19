from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json

User = Account()
# Create your views here.

#funtion loads the home page
def index(request):
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

#function loads the forgot password page
def Forgot_password(request):
    if request.POST:
        code = request.POST['code']
        password = request.POST['password']
        User.Forgot_Password(code, password)
        return redirect('login')
    else:
        return render(request, 'forgot_pass.html')
#function loads the staff page
def Staff_fun(request):
    content = User.Staff_data()
    return render(request, 'staff.html', content)

#function loads the client page
def Client_fun(request):
    content = User.client_data()
    return render(request, 'client.HTML', content)


def process_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Parse JSON
            #'user_id' : selectedclient, 'id' : selectedRoomid, 'price' : total, 'payment' : paymentmethod, 'service' : service
            data:dict = data
            
            user_id, data_id, price, paymentmethod, service, days= int(data['user_id']), int(data['id']), float(data['price']), data['payment'], int(data['service']), int(data['days'])

            if str(data_id)[0] == '1':
                #booking
                checkin = dt.date.today()
                checkout = checkin + dt.timedelta(days=days)
    
                booking_id = User.Book_room(user_id, data_id, str(checkin), str(checkout), price)
                User.Payment(user_id, price, paymentmethod, service_id=service, booking_id=booking_id)
            else:
                #service
                User.Book_service(data_id)
                User.Payment(user_id, price, paymentmethod, service_id=service)

            return JsonResponse({}, status=204)  # 204 No Content (No response)
        except json.JSONDecodeError:
            return JsonResponse({}, status=400)  # Bad Request if JSON is invalid

    return JsonResponse({}, status=405)