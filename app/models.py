from django.db import models
import random
import datetime as dt

# Create your models here.
class Booking(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    booking_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    check_in_date = models.TextField(blank=True, null=True, max_length=10)
    check_out_date = models.TextField(blank=True, null=True, max_length=10)
    number_of_guests = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True, max_length=200)
    booking_status = models.TextField( max_length=200)

    class Meta:
        managed = False
        db_table = 'Booking'

class Client(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=True, null=True, max_length=200)
    last_name = models.CharField(blank=True, null=True, max_length=200)
    contact = models.IntegerField()
    id_no = models.IntegerField(unique=True)
    email = models.CharField(blank=True, null=True, max_length=200)
    gender = models.TextField(max_length=200)  # This field type is a guess.
    password = models.CharField(blank=True, null=True, max_length=200)
    code = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'Client'

class Inventory(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    inventory_id = models.AutoField(primary_key=True)
    item_name = models.CharField(blank=True, null=True, max_length=200)
    category = models.CharField(blank=True, null=True, max_length=200)
    service_time = models.TextField(blank=True, null=True, max_length=20)
    item_description = models.TextField(blank=True, null=True, max_length=200)
    quantity = models.IntegerField(blank=True, null=True)
    price_per_unit = models.FloatField(blank=True, null=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'Inventory'

class Room(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField( max_length=200)
    bed_type = models.CharField(max_length=200)
    price_per_night = models.FloatField( max_length=200)
    availabilty_status = models.IntegerField()
    max_occupation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Room'

class Service(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=200)
    service_description = models.TextField(blank=True, null=True, max_length=200)
    service_price = models.FloatField(blank=True, null=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'Service'

class ServiceRequest(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    request_id = models.AutoField(primary_key=True)
    booking_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    request_time = models.TextField(blank=True, null=True, max_length=10)
    request_date = models.TextField(blank=True, null=True, max_length=10)
    request_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'Service_request'

class Staff(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=True, null=True, max_length=200)
    last_name = models.CharField(blank=True, null=True, max_length=200)
    contact = models.IntegerField()
    id_no = models.IntegerField(unique=True)
    email = models.CharField(blank=True, null=True, max_length=200)
    role = models.CharField(blank=True, null=True, max_length=200)
    service_id = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField()
    date_of_joining = models.DateField( max_length=200)
    shift_start = models.TimeField( max_length=200)
    shift_end = models.TimeField( max_length=200)
    gender = models.TextField( max_length=200)  # This field type is a guess.
    password = models.CharField(blank=True, null=True, max_length=200)
    code = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'Staff'

class Payment(models.Model):
    id = models.TextField(blank=True, null=True, max_length=200)  # This field type is a guess.
    payment_id = models.AutoField(primary_key=True)
    booking_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True, max_length=200)
    payment_time = models.TextField(blank=True, null=True, max_length=10)
    payment_date = models.TextField(blank=True, null=True, max_length=10)
    payment_mode = models.TextField( max_length=200)
    account = models.IntegerField()
    payment_status = models.TextField( max_length=200)

    class Meta:
        managed = False
        db_table = 'payment'

class Account:
    def __init__(self) -> None:
        self.user:int = 0
    
    def Auth(self, email, password):
        if '@havenhub' in str(email):
            if Staff.objects.filter(email=email).exists():
                if Staff.objects.filter(password=password).exists():
                    return True
            
        else:
            if Client.objects.filter(email=email).exists():
                if Client.objects.filter(password=password).exists():
                    return True

        return False
    
    def Register(self, f_name, l_name, email, id_no, contact, gender, password):
        if not Client.objects.filter(email=email).exists():
            length = len(list(Client.objects.values()))
            client_id = 3214 + length

            code = random.randrange(2000, 9999)
            while Client.objects.filter(code = code).exists():
                code = random.randrange(2000, 9999)

            client = Client(client_id = client_id, first_name = f_name, last_name = l_name, contact = contact, id_no = id_no, email = email, gender = gender, password = password, code = code)
            client.save()
            return True
        return False

    def Forgot_Password(self, code, new_pass):
        if str(code)[0] == "1":
            data=Staff.objects.filter(code=code)
            print(list(data))
            data.update(password=new_pass)
        else:
            data=Client.objects.filter(code=code)
            print(list(data))
            data.update(password=new_pass)

    def Book_room(self, client_id, room_id, check_in_date, check_out_date, no_guest, price):
        length = len(list(Booking.objects.values()))
        booking_id = 2133 + length
        check_in_date = dt.datetime.strptime(check_in_date, '%Y-%m-%d')
        check_out_date = dt.datetime.strptime(check_out_date, '%Y-%m-%d')
        book = Booking(booking_id=booking_id, client_id=client_id, room_id=room_id, check_in_date=check_in_date, check_out_date=check_out_date, number_of_guests=no_guest, total_price=price)
        book.save()
        Room.objects.filter(room_id=room_id).update(availability_status=1)

    def Reset(self):
        current_date = dt.date.today()
        book=Booking.objects.filter(check_out_date__lte=current_date)
        rooms = []
        for room in list(book):
            Room.objects.filter(room_id=room.room_id).update(availability_status=0)

        book.update(booking_status='complete')

    def Book_service(self, service_id, booking_id = None, request_date=dt.date.today()):
        length = len(list(ServiceRequest.objects.values()))
        request_id = 5003 + length
        service = ServiceRequest(request_id=request_id, booking_id=booking_id, request_date=request_date)
        service.save()

    def Staff_data(self):
        staff:dict = list(Staff.objects.filter(staff_id=self.user).values())[0]
        service_id = staff['service_id']

        services:dict = list(ServiceRequest.objects.filter(service_id=service_id).values())
        if len(services) != 0:
            for service in services:
                additions:dict = list(ServiceRequest.objects.filter(service_id=service_id))[0]
                service.update(additions) 

        print(services)
        return {'staff':staff, 'service':services}
