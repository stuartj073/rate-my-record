import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def landing():
    reviews = mongo.db.reviews.find()
    return render_template("landing_page.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the user is already
        # in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("User already exists")
            return redirect(url_for('register'))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        # insert new user into database
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"]= request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for('landing'), username=session["user"])

    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                flash("Incorrect password")
                return redirect(url_for('login'))
        
        else:
            #username doesn't exist
            flash("username doesn't exist")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # put user into session and return 
    # profile page as soon as they register
    username = mongo.db.users.find_one(
        {"username":session["user"]})["username"]

    if session["user"]:
        return render_template('profile.html', username=username)


@app.route("/logout")
def logout():
    # allow user to log out
    # by utilising the pop method
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for('login'))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "album_name": request.form.get("album"),
            "artist_name": request.form.get("artist"),
            "desc": request.form.get("desc"),
            "label": request.form.get("label"),
            "location": request.form.get("location"),
            "img": request.form.get("image"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Task successfully added")
        return redirect(url_for('add_review'))
    
    return render_template("add_review.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# Remember to remove debug = True prior to 
# project submission !!