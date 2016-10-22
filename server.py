"""Alaap Music Academy"""
from jinja2 import StrictUndefined
#from sqlalchemy import func

from flask import Flask, render_template, request, redirect, flash, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension
#from xml.dom.minidom import parse, parseString

# from model import connect_to_db, db, School, User, Neighborhood, Images, CostOfLiving, PriceItems, Crime, Favorites 
# from pyzipcode import ZipCodeDatabase


# from helper import find_zipcode_from_input, get_city_images, get_schools, row2dict 
from helper import hash_password

import requests
import os


app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def index():
    """Homepage."""
    return render_template("index.html")


@app.route('/courses')
def show_courses():
    return render_template("courses.html")


@app.route('/about_us')
def show_about_us():
    return render_template("about_us.html")





















@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""
    
    # Get form variables
    email = request.form.get("email")
    password = request.form.get("password")
    password_hashed = hash_password(password)
    zipcode = request.form.get("zipcode")
    zipcode = int(zipcode)

    new_user = User(email=email, password=password_hashed, zipcode=zipcode)

    db.session.add(new_user)
    db.session.commit()

    flash("Welcome to Help Me Relocate!")
    return redirect("/")


@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("You are not registered. Please register and then Login")
        return render_template("register_form.html")

    if user.password != hash_password(password):
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    # flash("You are now Logged in")
    return redirect("/")


@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    # flash("You are now logged Out.")
    return redirect("/")



if __name__ == "__main__":

    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    # app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host='0.0.0.0', debug=True)

