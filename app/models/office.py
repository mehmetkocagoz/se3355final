import sqlite3

class Office:
    def __init__(self, city,title, address, phone_number):
        self.city = city
        self.title = title
        self.address = address
        self.phone_number = phone_number

def connect():
        # Establish a connection to the SQLite database
        return sqlite3.connect("database.sqlite")

def list_of_offices(user_city):
    connection = connect()
    cursor = connection.cursor()
    if isinstance(user_city, tuple):
        user_city = user_city[0]
    
    cursor.execute("SELECT office_city,office_title,office_address,office_number FROM office WHERE office_city = ?",(user_city,))

    list_of_offices = cursor.fetchall()

    offices = []
    for row in list_of_offices:
        office = Office(*row)
        offices.append(office)

    connection.commit()
    connection.close()
    return offices

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

def city_id_query(user_city):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("SELECT city_id FROM city WHERE city_name = ?",(user_city,))

    city_id = cursor.fetchone()

    connection.commit()
    connection.close()
    return city_id

def town_list_query(city_id):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM city_town WHERE city_id = ?",(city_id,))

    town_list = cursor.fetchall()

    connection.commit()
    connection.close()
    return town_list

def lat_long_query(town_name):
    connection = connect()
    cursor = connection.cursor()
    
    cursor.execute("SELECT latitude, longitude FROM city_town WHERE town = ?",(town_name,))

    info = cursor.fetchall()

    connection.commit()
    connection.close()
    return info