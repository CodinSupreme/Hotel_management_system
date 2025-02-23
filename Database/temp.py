import sqlite3 as sql
import datetime as dt
location= r"C:\Users\Owner\Documents\coding\hotel_management_system\Database\test\Hotel_management_database.db"

def Create_tables():
    connector = sql.Connection(location)
    cursor = connector.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.execute("""CREATE TABLE Client(
                        id INT AUTO INCREMENT,
                        client_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        first_name VARCHAR(30),
                        last_name VARCHAR(30),
                        contact INTEGER NOT NULL,
                        id_no INTEGER NOT NULL UNIQUE,
                        email VARCHAR(100),
                        gender NOT NULL CHECK(gender IN ('Male', 'Female', 'Other')),
                        password VARCHAR(20),
                        code INTEGER UNIQUE NOT NULL 
                )""")

    cursor.execute("""CREATE TABLE Staff(
                        id INT AUTO INCREMENT,
                        staff_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        first_name VARCHAR(30),
                        last_name VARCHAR(30),
                        contact INTEGER NOT NULL,
                        id_no INTEGER NOT NULL UNIQUE,
                        email VARCHAR(100),
                        role VARCHAR(30),
                        salary INTEGER NOT NULL,
                        date_of_joining DATE NOT NULL,
                        shift_start TIME NOT NULL,
                        shift_end TIME NOT NULL,
                        gender NOT NULL CHECK(gender IN ('Male', 'Female', 'Other')),
                        password VARCHAR(20),
                        code INTEGER UNIQUE NOT NULL 
                )""")

    cursor.execute("""CREATE TABLE Inventory(
                        id INT AUTO INCREMENT,
                        inventory_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        item_name VARCHAR(60),
                        category VARCHAR(20),
                        item_description TEXT,
                        quantity INTEGER DEFAULT 0,
                        price_per_unit REAL DEFAULT 0.00
                )""")

    cursor.execute("""CREATE TABLE Room(
                        id INT AUTO INCREMENT,
                        room_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        room_type VARCHAR(50) NOT NULL,
                        bed_type VARCHAR(50) NOT NULL,
                        price_per_night REAL NOT NULL,
                        availabilty_status  INTEGER NOT NULL DEFAULT 1 CHECK(availabilty_status IN (0, 1)),
                        max_occupation INTEGER NOT NULL
                )""")

    cursor.execute("""CREATE TABLE Booking(
                        id INT AUTO INCREMENT,
                        booking_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        client_id INTEGER,
                        room_id INTEGER,
                        check_in_date DATE NOT NULL,
                        check_out_date DATE NOT NULL,
                        number_of_guests INTEGER DEFAULT 1,
                        total_price REAL,
                        booking_status TEXT NOT NULL DEFAULT 'pending' CHECK(booking_status IN ('pending', 'active', 'complete'))     
                )""")

    cursor.execute("""CREATE TABLE Service(
                        id INT AUTO INCREMENT,
                        service_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        service_name VARCHAR(100) NOT NULL,
                        service_description TEXT,
                        service_price REAL   
                )""")

    cursor.execute("""CREATE TABLE Service_request(
                        id INT AUTO INCREMENT,
                        request_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        booking_id INTEGER,
                        service_id INTEGER,
                        request_date DATE,
                        request_status TEXT NOT NULL DEFAULT 'pending' CHECK(request_status IN ('pending', 'active'))
                )""")

    cursor.execute("""CREATE TABLE payment(
                        id INT AUTO INCREMENT,
                        payment_id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                        booking_id INTEGER,
                        service_id INTEGER,
                        amount REAL,
                        payment_date DATE,
                        payment_mode TEXT NOT NULL DEFAULT 'M-pesa' CHECK(payment_mode IN ('M-pesa', 'Bank')),
                        account INTEGER NOT NULL,
                        payment_status TEXT NOT NULL DEFAULT 'not paid' CHECK(payment_status IN ('not paid', 'pending', 'paid'))
                )""")
    
    connector.commit()
    connector.close()

def insert_client(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO client(client_id, first_name, last_name, contact, id_no, email, gender, password) VALUES(?, ?, ?,?,?,?,?,?)", x)
     connector.commit()
     connector.close()

def insert_staff(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO staff(staff_id, first_name, last_name, contact, id_no, email, role, salary, date_of_joining, shift_start, shift_end, gender, password) VALUES(?, ?, ?,?,?,?,?,?,?,?,?,?,?)", x)
     connector.commit()
     connector.close()

def insert_invent(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO inventory(inventory_id, item_name, category, item_description, quantity, price_per_unit) VALUES(?, ?, ?,?,?,?)", x)
     connector.commit()
     connector.close()

def insert_service(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO Service(service_id, service_name, service_description, service_price) VALUES(?, ?, ?,?)", x)
     connector.commit()
     connector.close()

def insert_Room(x:list):
     connector = sql.Connection(location)
     cursor = connector.cursor()
     cursor.executemany("INSERT INTO Service(room_id, room_type, bed_type, price_per_night, availability_status, max_occupation) VALUES(?, ?, ?,?,?,?)", x)
     connector.commit()
     connector.close()

def update():
     conn = sql.connect(r"C:\Users\Owner\Documents\coding\hotel_management_system\Database\Hotel_management_database.db")
     cur = conn.cursor()
     cur.execute("ALTER TABLE Inventory ADD COLUMN service_time VARCHAR(20) ")     
     conn.commit()
     conn.close()   


insert_staff([1241,'Tiffany', 'bradly', 754215422, 13231, 'tiffanyb@gmail.com', 'receptionist', 20000, dt.datetime.strptime('2025-02-21', '%Y-%m-%d'), dt.datetime.strptime('07:00:00', '%H:%M:%S'), dt.datetime.strptime('12:00:00', '%H:%M:%S'), 'Female', 'Tiffany123'])
