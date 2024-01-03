from flask import render_template,request,redirect, url_for,session
from app import app
from app.vehiclecontroller import getAll
from app.officecontroller import insertDataToTable
from app.usercontroller import checkUserPasswordForRegisteration,createNewUser,checkUsernamePasswordForLogin

app.secret_key = 'secret_key'

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # Access form data
        username = request.form.get('username')
        password = request.form.get('password')

        # Controller will check credentials
        if checkUsernamePasswordForLogin(username,password) == True:
            session['current_user'] = username
            return redirect(url_for('home'))
        else:
            wrong_credentials_error = "Wrong username password!"
            return render_template('login.html',error=wrong_credentials_error)

@app.route('/register',methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # Access form data
        username = request.form.get('username')
        password = request.form.get('password')
        password_again = request.form.get('passwordAgain')
        selected_country = request.form.get('countries')
        selected_city = request.form.get('cities')

        # Passwords should match!
        # Controller will take action here!
        if checkUserPasswordForRegisteration(password,password_again) == False:
            match_error = "Passwords should match!"
            return render_template('register.html',message = match_error)
        # If passwords match
        # New user will create in the database
        # Home page will be redirected
        else:
            createNewUser(username,password,selected_country,selected_city)
            session['current_user'] = username
            return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Clear the user session
    session.pop('current_user', None)
    
    # Redirect to the home page or any other page after logout
    return redirect(url_for('home'))

@app.route('/')
def homepage():
    username = session.get('current_user','Guest')
    return render_template('index.html',current_user = username)

# Render with all vehicles in the database
@app.route('/home',methods= ['GET','POST'])
def home():
    if request.method == 'GET':
        username = session.get('current_user','Guest')
        return render_template('index.html',current_user = username)
    else:
        pickup_office = request.form.get('pickupOffice')
        return_office = request.form.get('returnOffice')
        pickup_date = request.form.get('DatePicker')
        pickup_time = request.form.get('pickupHour')
        return_date = request.form.get('DatePicker2')
        return_time = request.form.get('returnHour')

        # Process the form data (you can save it to a database, etc.)
        # For now, just print the values to the console
        print('Pickup Office:', pickup_office)
        print('Return Office:', return_office)
        print('Pickup Date:', pickup_date)
        print('Pickup Time:', pickup_time)
        print('Return Date:', return_date)
        print('Return Time:', return_time)

        # You can redirect to a thank you page or return a response
        return "Form submitted successfully!"

@app.route('/rent')
def rent():
    vehicle_data = getAll()
    return render_template('rent.html',vehicle_list = vehicle_data)