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

    cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()

    connection.commit()
    connection.close()
    
    return True if user else False

def findUserCity(username):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT city FROM user WHERE username = ?",(username))

    user_city = cursor.fetchone()

    connection.commit()
    connection.close()

    return user_city