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

