"""
authentication
"""

from flask import Blueprint, render_template 

auth = Blueprint('auth', __name__) # Define blueprint

@auth.route('/login')
def login():
    return render_template("login.html", text="Testing")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/home')
def home():
    return render_template("home.html")