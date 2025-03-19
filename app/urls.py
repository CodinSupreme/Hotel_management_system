from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('staff', views.Staff_fun, name='staff'),
    path('client', views.Client_fun, name='client'),
    path('forgot_pass', views.Forgot_password, name='forgot_password'),
    path('api/process-data/', views.process_data, name='process_data'),
]