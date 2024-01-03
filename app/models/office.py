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