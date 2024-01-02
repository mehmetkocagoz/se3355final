import sqlite3

class User():
    def __init__(self,ID,username,password,country,city):
        self.ID = ID
        self.username = username
        self.password = password
        self.country = country
        self.city = city

# Connect to database
def connect():
    return sqlite3.connect("database.sqlite")

# Creates a user
def insertUserToDatabase(username,password,country,city):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO user(username,password,country,city) VALUES (?,?,?,?)",(username,password,country,city))

    connection.commit()
    connection.close()

def checkUser(username,password):
    connection = connect()
    cursor = connection.cursor()

    connection.commit()
    connection.close()