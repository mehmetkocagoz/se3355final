from flask import render_template,request,redirect, url_for,session
from app import app,flow
from app.controllers.vehiclecontroller import getAllWithOffice,getAllVehicles,order_vehicle_list
from app.controllers.officecontroller import takeOfficeListFromDatabase,takeOfficesCarListFromDatabase,takeCityIdFromDatabase,takeTownListFromDatabase,takeLatLong
from app.controllers.usercontroller import checkUserPasswordForRegisteration,createNewUser,checkUsernamePasswordForLogin,takeUserCityFromDatabase,formatBy
from app.controllers.distancecalculator import calculate_distance
from pip._vendor import cachecontrol
import google.auth.transport.requests
from google.oauth2 import id_token
import requests


app.secret_key = 'secret_key'

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # Access form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Controller will check credentials
        status , user_name = checkUsernamePasswordForLogin(email,password)
        if status == True:
            session['current_user'] = user_name
            user_city = takeUserCityFromDatabase(user_name)
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
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        password_again = request.form.get('passwordAgain')
        selected_country = request.form.get('countries')
        selected_city = request.form.get('cities')

        # Passwords should match!
        # Controller will take action here!
        status,error = checkUserPasswordForRegisteration(password,password_again)
        if status == False:
            return render_template('register.html',message = error)
        # If passwords match
        # New user will create in the database
        # Home page will be redirected
        else:
            createNewUser(email,username,password,selected_country,selected_city)
            session['current_user'] = username
            selected_city = formatBy(selected_city)
            session['user_city'] = selected_city
            return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Clear the user session
    session.clear()
    # Redirect to the home page or any other page after logout
    return redirect(url_for('home'))


# Configure logging
import logging
logging.basicConfig(level=logging.DEBUG)
@app.route('/google-login')
def googleLogin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    logging.debug("Redirecting to Google authorization URL: %s", authorization_url)
    return redirect(authorization_url)

@app.route("/.auth/login/google/callback")
def googleCallback():
    logging.debug("Received callback request with URL: %s", request.url)
    try:
        flow.fetch_token(authorization_response=request.url)
    except Exception as e:
        logging.error("Error fetching token: %s", str(e))
        # Handle the error as needed, e.g., redirect to an error page

    if not session["state"] == request.args["state"]:
        logging.error("State mismatch. Redirecting to login.")
        return redirect(url_for('login'))

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    # token_request and credentials._id_token will be used for verification
    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request
    )
    # I will just use name attribute of id_info
    # It returns as name attribute from Google
    # User_city is not include in Google
    # Therefore I will ask user city later
    user_name = id_info['name']
    session['current_user'] = user_name

    logging.info("State matched. Redirecting to home.")
    return redirect(url_for('home'))

@app.route('/')
def homepage():
    return redirect(url_for('home'))

# Render with all vehicles in the database
@app.route('/home',methods= ['GET','POST'])
def home():
    if request.method == 'GET':
        username = session.get('current_user','Guest')
        user_city = session.get('user_city','DENİZLİ')
        session['current_user'] = username
        session['user_city'] = user_city
        office_list_for_user_city = takeOfficeListFromDatabase(user_city)
        city_id = takeCityIdFromDatabase(user_city)
        town_list = takeTownListFromDatabase(city_id)
        # Denizli city_id == 1
        if city_id == 1:
            closest_offices = calculate_distance("MERKEZ",town_list)
            session['town'] = "MERKEZ"
        else:
            closest_offices = calculate_distance("ALSANCAK",town_list)
            session['town'] = "ALSANCAK"
        town_name = session.get('town')
        latitude, longitude = takeLatLong(town_name)
        google_maps_url = f'https://maps.google.com/maps?q={latitude},{longitude}&hl=en;z=14&output=embed'    
        session['closest_offices'] = closest_offices
        return render_template('index.html',current_user = username,office_list = office_list_for_user_city,town_list = closest_offices,google_maps_url=google_maps_url)
    else:
        if 'city_update' in request.form:
            selected_city = request.form['city_update']
            if selected_city != "SAME":
                session['user_city'] = selected_city
                print(selected_city)
                if selected_city == "İZMİR":
                    session['town'] = "ALSANCAK"
                else:
                    session['town'] = "MERKEZ"
            else:
                selected_city = session.get('user_city')
            username = session.get('current_user','Guest')
            office_list_for_user_city = takeOfficeListFromDatabase(selected_city)
            city_id = takeCityIdFromDatabase(selected_city)
            town_list = takeTownListFromDatabase(city_id)
            

            selected_town = request.form['town_update']
           
            if selected_town != "SAME":
                closest_offices = calculate_distance(selected_town,town_list)
                latitude,longitude = takeLatLong(selected_town)
                session['closest_offices'] = closest_offices
            elif selected_town == "SAME":
                town_name = session.get('town')
                latitude, longitude = takeLatLong(town_name)
                closest_offices = session.get('closest_offices')
            
            google_maps_url = f'https://maps.google.com/maps?q={latitude},{longitude}&hl=en;z=14&output=embed'    
            return render_template('index.html',current_user = username,office_list = office_list_for_user_city,user_city=selected_city,town_list = town_list,google_maps_url=google_maps_url)
        else:
            pickup_office = request.form.get('pickupOffice')
            return_office = request.form.get('returnOffice')
            pickup_date = request.form.get('DatePicker')
            pickup_time = request.form.get('pickupHour')
            return_date = request.form.get('DatePicker2')
            return_time = request.form.get('returnHour')

            session['pickupOffice'] = pickup_office
            session['pickup_date'] = pickup_date
            session['pickup_time'] = pickup_time
            session['return_date'] = return_date
            session['return_time'] = return_time
            return redirect(url_for('rent'))

@app.route('/rent',methods = ['GET','POST'])
def rent():
    # We should look which cars pickup_office has
    # And render the rent.html with these cars
    pickup_office = session.get('pickupOffice','ALL')
    car_id_list = takeOfficesCarListFromDatabase(pickup_office)
    vehicle_data = getAllWithOffice(car_id_list)
    if request.method == 'GET':
        if pickup_office == 'ALL':
            vehicle_data = getAllVehicles()
         
        return render_template('rent.html', vehicle_list = vehicle_data)
    else:
        car_type = request.form.get('vehicleType')
        price_order = request.form.get('price')
        transmission_type = request.form.get('transmissionType')

        ordered_vehicle_list = order_vehicle_list(car_type,price_order,transmission_type,vehicle_data)
        return render_template('rent.html',vehicle_list = ordered_vehicle_list)