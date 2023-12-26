import sqlite3
import base64

class Vehicle():
    def __init__(self,ID,CarType,Brand,Model,Transmission,FuelType,DepositPrice,DailyRentPrice,DefaultKM,Image):
        self.ID = ID
        self.CarType = CarType
        self.Brand = Brand
        self.Model = Model
        self.Transmission = Transmission
        self.FuelType = FuelType
        self.DepositPrice = DepositPrice
        self.DailyRentPrice = DailyRentPrice
        self.DefaultKM = DefaultKM
        self.Image = Image

# Connect to database
def connect():
    return sqlite3.connect("database.sqlite")

def getAllVehicles():
    # First connect to database
    connection = connect()

    try:
        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the SQL query to retrieve all vehicles
        cursor.execute('''
            SELECT ID, CarType, Brand, Model, Transmission, FuelType, 
                   DepositPrice, DailyRentPrice, DefaultKM, Image
            FROM VEHICLE
        ''')
        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Convert the rows into a list of Vehicle objects
        vehicles = []
        for row in rows:
            vehicle = Vehicle(*row)
            vehicles.append(vehicle)

        return vehicles

    except sqlite3.Error as e:
        print("Error retrieving vehicles:", e)

    finally:
        # Close the connection
        connection.close()

# Create a table
def createTable():
    connection = connect()
    cursor = connection.cursor()
    # Creating a table for vehicles
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS OFFICE (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Address TEXT NOT NULL,
    PhoneNumber TEXT NOT NULL,
    Latitude REAL NOT NULL,
    Longitude REAL NOT NULL
    );
    ''')
    connection.commit()
    connection.close()
# Insert data into the table
def insertData():
    connection = connect()
    cursor = connection.cursor()
    title = ""
    address = ""
    phone_number = ""
    latitude = ""
    longitude = ""

    # Insert data into the OFFICE table
    cursor.execute('''
    INSERT INTO OFFICE (Title, Address, PhoneNumber, Latitude, Longitude)
    VALUES (?, ?, ?, ?, ?);
    ''', (title, address, phone_number, latitude, longitude))

    connection.commit()
    connection.close()
