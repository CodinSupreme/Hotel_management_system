from django.contrib import admin
from .models import *

# Register your models here.
class Client_admin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'contact', 'id_no', 'email', 'gender', 'code']

class Staff_admin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'contact', 'id_no', 'email', 'gender', 'role', 'salary', 'date_of_joining', 'shift_start', 'shift_end', 'code']

class Rooms_admin(admin.ModelAdmin):
    list_display = ['room_id', 'room_type', 'bed_type', 'price_per_night', 'availabilty_status', 'max_occupation']

class inventory_admin(admin.ModelAdmin):
    list_display = ['inventory_id', 'item_name', 'category', 'item_description', 'quantity', 'price_per_unit']

class Service_admin(admin.ModelAdmin):
    list_display = ['service_id', 'service_name', 'service_description', 'service_price']

class ServiceRequest_admin(admin.ModelAdmin):
    list_display = ['request_id', 'booking_id', 'service_id', 'request_date', 'request_status']

class Payment_admin(admin.ModelAdmin):
    list_display = ['payment_id', 'amount', 'payment_mode', 'booking_id', 'service_id', 'payment_time', 'payment_date', 'payment_status']

class Booking_admin(admin.ModelAdmin):
    list_display = ['client_id', 'booking_id', 'room_id', 'check_in_date', 'check_out_date', 'total_price', 'booking_status']

admin.site.register(Client, Client_admin)
admin.site.register(Staff, Staff_admin)
admin.site.register(Room, Rooms_admin)
admin.site.register(Inventory, inventory_admin)
admin.site.register(Service, Service_admin)
admin.site.register(ServiceRequest, ServiceRequest_admin)
admin.site.register(Payment, Payment_admin)
admin.site.register(Booking, Booking_admin)
