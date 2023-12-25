from flask import render_template
from app import app
from app.controller import getAll


@app.route('/login')
def login():
    return render_template('login.html')

# Render with all vehicles in the database
@app.route('/')
def home():
    vehicle_data = getAll()
    return render_template('index.html')