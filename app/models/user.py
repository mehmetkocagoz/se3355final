import sqlite3

class User():
    def __init__(self,ID,email,username,password,country,city):
        self.ID = ID
        self.email = email
        self.username = username
        self.password = password
        self.country = country
        self.city = city

# Connect to database
def connect():
    return sqlite3.connect("database.sqlite")

# Creates a user
def insertUserToDatabase(email,username,password,country,city):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO user(email,username,password,country,city) VALUES (?,?,?,?,?)",(email,username,password,country,city,))

    connection.commit()
    connection.close()

def checkUser(email,password):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT username FROM user WHERE email = ? AND password = ?", (email, password,))
    user = cursor.fetchone()
    
    connection.commit()
    connection.close()

    if user == None:
        return False, None
    else:
        return True,user

def findUserCity(username):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT city FROM user WHERE username = ?",(username,))

    user_city = cursor.fetchone()

    connection.commit()
    connection.close()

    return user_city