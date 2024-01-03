import sqlite3

class Office:
    def __init__(self, title, address, phone_number, latitude, longitude):
        self.title = title
        self.address = address
        self.phone_number = phone_number
        self.latitude = latitude
        self.longitude = longitude

def connect():
        # Establish a connection to the SQLite database
        return sqlite3.connect("database.sqlite")

def createTables():
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   password TEXT,
                   country TEXT,
                   city TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS city(
                   city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   city_name TEXT,
                   latitude REAL,
                   longtitude REAL
        );
                   ''')

     # Create Office Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS office (
            office_id INTEGER PRIMARY KEY AUTOINCREMENT,
            office_city TEXT,
            office_title TEXT,
            office_address TEXT,
            office_number TEXT
        );
    ''')

    # Create CarOfficeAssignment Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS car_office_assignment (
            car_id INTEGER,
            office_id INTEGER,
            PRIMARY KEY (car_id, office_id),
            FOREIGN KEY (car_id) REFERENCES car(car_id),
            FOREIGN KEY (office_id) REFERENCES office(office_id)
        );
    ''')

    # Create Rental Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rental (
            rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER,
            office_id INTEGER,
            rental_start_date TEXT,
            rental_end_date TEXT,
            FOREIGN KEY (car_id) REFERENCES car(car_id),
            FOREIGN KEY (office_id) REFERENCES office(office_id)
        );
    ''')
    connection.commit()
    connection.close()

def insertCarOffice():
     connection = connect()
     cursor = connection.cursor()
     car_id = 10
     office_id = 5
     cursor.execute('''
    INSERT INTO car_office_assignment (car_id, office_id)
    VALUES (?, ?)
''', (car_id, office_id))
     connection.commit()
     connection.close()

# Insert data into the table
def insertData():
    connection = connect()
    cursor = connection.cursor()
    city = "DENİZLİ"
    title = "HAVALİMANI OFİSİ"
    address = "Selim Paşa Cd. Selim Mh. No:9 45000 Selimiye/Denizli"
    phone_number = "0205 555 33 33"

    # Insert data into the OFFICE table
    cursor.execute('''
    INSERT INTO OFFICE (office_city, office_title, office_address, office_number)
    VALUES (?, ?, ?, ?);
    ''', (city, title, address, phone_number))

    connection.commit()
    connection.close()

def insertCity():
    connection = connect()
    cursor = connection.cursor()
    city = "İZMİR"
    latitude = 38.423733
    longtitude = 27.142826
    cursor.execute('''
INSERT INTO city(city_name,latitude,longtitude)
                   VALUES (?,?,?);
                   ''',(city,latitude,longtitude))
    connection.commit()
    connection.close()

def list_of_offices(user_city):
    connection = connect()
    cursor = connection.cursor()
    if isinstance(user_city, tuple):
        user_city = user_city[0]
    print(user_city)
    cursor.execute("SELECT * FROM office WHERE office_city = ?",(user_city,))

    list_of_offices = cursor.fetchall()

    connection.commit()
    connection.close()
    return list_of_offices

def office_id_query(pickup_office):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT office_id FROM office WHERE office_title = ?",(pickup_office,))

    office_id = cursor.fetchone()

    connection.commit()
    connection.close()
    return office_id

def car_id_list_query(office_id):
    connection = connect()
    cursor = connection.cursor()
    office_id_value = office_id[0]
    cursor.execute("SELECT car_id FROM car_office_assignment WHERE office_id = ?",(office_id_value,))

    car_id_list = cursor.fetchall()

    connection.commit()
    connection.close()
    return car_id_list