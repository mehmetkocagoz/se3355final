from app.user import insertUserToDatabase,checkUser

def checkUserPasswordForRegisteration(password,password_again):
    if password != password_again:
        return False
    else:
        return True

# There is no business logic    
def createNewUser(username,password,country,city):
    insertUserToDatabase(username,password,country,city)

# There is no business logic
def checkUsernamePasswordForLogin(username,password):
    return checkUser(username,password)
    
    