from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
]