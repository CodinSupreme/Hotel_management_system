# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Booking(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    booking_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(blank=True, null=True)
    room_id = models.IntegerField(blank=True, null=True)
    check_in_date = models.TextField(blank=True, null=True)
    check_out_date = models.TextField(blank=True, null=True)
    number_of_guests = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    booking_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'Booking'


class Client(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    contact = models.IntegerField()
    id_no = models.IntegerField(unique=True)
    email = models.CharField(blank=True, null=True)
    gender = models.TextField()  # This field type is a guess.
    password = models.CharField(blank=True, null=True)
    code = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'Client'


class Inventory(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    inventory_id = models.AutoField(primary_key=True)
    item_name = models.CharField(blank=True, null=True)
    category = models.CharField(blank=True, null=True)
    service_time = models.TextField(blank=True, null=True)
    item_description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price_per_unit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Inventory'


class Room(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    room_id = models.AutoField(primary_key=True)
    room_type = models.CharField()
    bed_type = models.CharField()
    price_per_night = models.FloatField()
    availabilty_status = models.IntegerField()
    max_occupation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Room'


class Service(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField()
    service_description = models.TextField(blank=True, null=True)
    service_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Service'


class ServiceRequest(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    request_id = models.AutoField(primary_key=True)
    booking_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    request_time = models.TextField(blank=True, null=True)
    request_date = models.TextField(blank=True, null=True)
    request_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'Service_request'


class Staff(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    contact = models.IntegerField()
    id_no = models.IntegerField(unique=True)
    email = models.CharField(blank=True, null=True)
    role = models.CharField(blank=True, null=True)
    salary = models.IntegerField()
    date_of_joining = models.DateField()
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    gender = models.TextField()  # This field type is a guess.
    password = models.CharField(blank=True, null=True)
    code = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'Staff'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Payment(models.Model):
    id = models.TextField(blank=True, null=True)  # This field type is a guess.
    payment_id = models.AutoField(primary_key=True)
    booking_id = models.IntegerField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_time = models.TextField(blank=True, null=True)
    payment_date = models.TextField(blank=True, null=True)
    payment_mode = models.TextField()
    account = models.IntegerField()
    payment_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'payment'
