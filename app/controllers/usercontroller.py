from app.models.user import insertUserToDatabase,checkUser,findUserCity

def checkUserPasswordForRegisteration(password,password_again):
    if password != password_again:
        return False,"Passwords Should Match"
    elif len(password)< 8 or not any(char.isdigit() for char in password) or not any(char.isalnum() for char in password):
        return False,"Invalid password. Please ensure it's at least 8 characters long, contains at least 1 number, and 1 alphanumeric character."
    else:
        return True


# There is no business logic    
def createNewUser(username,password,country,city):
    insertUserToDatabase(username,password,country,city)

# There is no business logic
def checkUsernamePasswordForLogin(username,password):
    return checkUser(username,password)
    
def takeUserCityFromDatabase(username):
    user_city = findUserCity(username)
    # Handle tuple
    # Convert it to Turkish alphabet format
    user_city = user_city[0]
    user_city = user_city.upper()
    user_city = user_city.replace('I','İ')
    return user_city