from flask import render_template,request
from app import app


@app.route('/login')
def login():
    
    return render_template('login.html')