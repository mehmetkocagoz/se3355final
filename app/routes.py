from flask import render_template,request,redirect, url_for,session
from app import app
from app.vehiclecontroller import getAll
from app.officecontroller import insertDataToTable,takeOfficeListFromDatabase,takeOfficesCarListFromDatabase
from app.usercontroller import checkUserPasswordForRegisteration,createNewUser,checkUsernamePasswordForLogin,takeUserCityFromDatabase

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
            user_city = takeUserCityFromDatabase(username)
            session['user_city'] = user_city
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
            session['user_city'] = selected_city
            return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Clear the user session
    session.pop('current_user', None)
    session.pop('user_city',None)
    # Redirect to the home page or any other page after logout
    return redirect(url_for('home'))

@app.route('/')
def homepage():
    username = session.get('current_user','Guest')
    user_city = session.get('user_city','DENİZLİ')
    office_list_for_user_city = takeOfficeListFromDatabase(user_city)
    return render_template('index.html',current_user = username,office_list = office_list_for_user_city)

# Render with all vehicles in the database
@app.route('/home',methods= ['GET','POST'])
def home():
    if request.method == 'GET':
        username = session.get('current_user','Guest')
        user_city = session.get('user_city','DENİZLİ')
        office_list_for_user_city = takeOfficeListFromDatabase(user_city)
        return render_template('index.html',current_user = username,office_list = office_list_for_user_city)
    else:
        pickup_office = request.form.get('pickupOffice')
        return_office = request.form.get('returnOffice')
        pickup_date = request.form.get('DatePicker')
        pickup_time = request.form.get('pickupHour')
        return_date = request.form.get('DatePicker2')
        return_time = request.form.get('returnHour')

        # We should look which cars pickup_office has
        # And render the rent.html with these cars
        car_id_list = takeOfficesCarListFromDatabase(pickup_office)
        vehicle_data = getAll(car_id_list)

        return render_template('rent.html',vehicle_list = vehicle_data)

@app.route('/rent')
def rent():
    
    return render_template('rent.html')