from flask import render_template
from app import app
from app.vehiclecontroller import getAll
from app.officecontroller import insertDataToTable


@app.route('/login')
def login():
    insertDataToTable()
    return render_template('login.html')

# Render with all vehicles in the database
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rent')
def rent():
    vehicle_data = getAll()
    return render_template('rent.html',vehicle_list = vehicle_data)