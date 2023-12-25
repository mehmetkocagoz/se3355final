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

# Insert data into the table
def insertData():
    connection = connect()
    cursor = connection.cursor()
    title = "İZMİR BUCA OFİSİ"
    address = "Ahmet Piriştina Cd. Yıldız Mh. No:9 35390 Buca/İzmir"
    phone_number = "0232 444 44 44"
    latitude = 38.4742423
    longitude = 27.2363015

    # Insert data into the OFFICE table
    cursor.execute('''
    INSERT INTO OFFICE (Title, Address, PhoneNumber, Latitude, Longitude)
    VALUES (?, ?, ?, ?, ?);
    ''', (title, address, phone_number, latitude, longitude))

    connection.commit()
    connection.close()
