"""
store main views or URL end points for front end
"""

from flask import Blueprint, render_template

views = Blueprint('views', __name__)  # Define blueprint


@views.route('/')
def home():
    return render_template("home.html")
