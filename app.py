"""
Imports used to connect to MongoDB, flask
and werkzeug
"""
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
    """
    generate list to allow iteration over
    the reviews collection more than once
    on each page
    """
    reviews = list(mongo.db.reviews.find())
    store_reviews = list(mongo.db.store_reviews.find())

    if not session:
        return render_template("landing_page.html", reviews=reviews,
                               store_reviews=store_reviews)
    user = mongo.db.users.find_one({"username": session["user"]})
    return render_template("landing_page.html", reviews=reviews,
                           store_reviews=store_reviews, user=user)


@app.route("/search_bar", methods=["GET", "POST"])
def search_bar():
    """
    Function for search form
    """
    search = request.form.get("search")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": search}}))
    store_reviews = list(mongo.db.store_reviews.find(
        {"$text": {"$search": search}}))
    return render_template("landing_page.html", reviews=reviews,
                           store_reviews=store_reviews)


@app.route("/about")
def about():
    """
    Renders about page
    """
    return render_template("about.html")


@app.route("/registe_user", methods=["GET", "POST"])
def register_user():
    """
    Renders page for new users
    to register their username and
    password
    """
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
        session["user"] = request.form.get("username").lower()
        flash("Registration successful")
        return redirect(url_for('landing', username=session["user"]))

    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Renders log in page for users
    """
    if request.method == "POST":
        # check if username exists
        # (taken from Tim Nelson's tutorial)
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                flash("Incorrect password")
                return redirect(url_for('login'))
        else:
            # username doesn't exist
            flash("username doesn't exist")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    put user into session and return
    profile page as soon as they register
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    reviews = list(mongo.db.reviews.find())
    store_reviews = list(mongo.db.store_reviews.find())
    if session["user"]:
        return render_template('profile.html', username=username,
                               reviews=reviews, store_reviews=store_reviews)

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    """
    allow user to log out
    by utilising the pop method
    """
    session.pop("user")
    flash("You have been logged out")
    return redirect(url_for('login'))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    """
    allow user to input values to
    keys in form
    """
    if request.method == "POST":
        review = {
            "album_name": request.form.get("album"),
            "artist_name": request.form.get("artist"),
            "desc": request.form.get("desc"),
            "label": request.form.get("label"),
            "location": request.form.get("location"),
            "img": request.form.get("image"),
            "genre": request.form.get("genre"),
            "date": request.form.get("date"),
            "created_by": session["user"],
            "wishlist": []
        }
        # post the session user's
        # review to the mongo db
        mongo.db.reviews.insert_one(review)
        flash("Review added")
        return redirect(url_for('add_review'))
    return render_template("add_review.html")


@app.route("/add_store_review", methods=["GET", "POST"])
def add_store_review():
    """
    add store review to db if
    request method is POST
    """
    if request.method == "POST":
        store_review = {
            "store_name": request.form.get("store-name"),
            "location": request.form.get("location"),
            "store_desc": request.form.get("store-desc"),
            "store_genre": request.form.get("genre-store"),
            "store_img": request.form.get("image-store"),
            "site_url": request.form.get("site-url"),
            "created_by": session["user"],
            "wishlist": []
        }
        # insert new store review to
        # mongo db
        mongo.db.store_reviews.insert_one(store_review)
        flash("Review added!")
        return redirect(url_for("add_store_review"))

    return render_template("add_store_review.html")


@app.route("/manage_reviews")
def manage_reviews():
    """
    Manage review page enlists all reviews
    made by all users to the site
    """
    reviews = mongo.db.reviews.find()
    store_reviews = mongo.db.store_reviews.find()
    return render_template("manage_reviews.html", reviews=reviews,
                           store_reviews=store_reviews)


@app.route("/manage_users")
def manage_users():
    """
    Manage users lists all
    users to the website
    """
    users = mongo.db.users.find()
    return render_template("manage_users.html", users=users)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    """
    Page for editing a users record
    review
    """
    if request.method == "POST":
        review = {
            "$set": {
                "album_name": request.form.get("album"),
                "artist_name": request.form.get("artist"),
                "desc": request.form.get("desc"),
                "label": request.form.get("label"),
                "location": request.form.get("location"),
                "img": request.form.get("image"),
                "date": request.form.get("date"),
                "genre": request.form.get("genre"),
                "created_by": session["user"]
            }
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, review)
        flash("Review updated")
    # locate the reviews in the database
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", review=review)


@app.route("/edit_store_review/<store_review_id>", methods=["GET", "POST"])
def edit_store_review(store_review_id):
    """
    Locates the reviews in the database
    """
    if request.method == "POST":
        store_review = {
            "$set": {
                "store_name": request.form.get("store-name"),
                "location": request.form.get("location"),
                "store_desc": request.form.get("store-desc"),
                "store_genre": request.form.get("genre-store"),
                "store_img": request.form.get("image-store"),
                "site_url": request.form.get("site-url"),
                "created_by": session["user"]
            }
        }
        mongo.db.store_reviews.update({"_id": ObjectId(store_review_id)},
                                      store_review)
        flash("Review updated")

    store_review = mongo.db.store_reviews.find_one({"_id": ObjectId
                                                   (store_review_id)})
    return render_template("edit_store_review.html", store_review=store_review)


@app.route("/review_page/<review_id>")
def review_page(review_id):
    """
    Individual review page
    """
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("review_page.html", review=review)


@app.route("/store_review_page/<store_review_id>")
def store_review_page(store_review_id):
    """
    Individual store review page
    """
    store_review = mongo.db.store_reviews.find_one({"_id": ObjectId
                                                   (store_review_id)})
    return render_template("store_review_page.html", store_review=store_review)


@app.route("/add_to_wishlist/<review_id>")
def add_to_wishlist(review_id):
    """
    Update 'wishlist' key of each record
    review with the current session username
    """
    user = mongo.db.users.find_one({"username": session["user"]})
    in_wishlist = mongo.db.reviews.find_one(
        {"_id": ObjectId(review_id), "wishlist": ObjectId(user["_id"])})
    # if user is not in review wishlist
    if not in_wishlist:
        mongo.db.reviews.find_one_and_update(
                        {"_id": ObjectId(review_id)},
                        {"$addToSet": {"wishlist": ObjectId(user["_id"])}})
        flash("Added to wishlist")
    else:
        flash("Review already in wishlist")

    return redirect(url_for("landing"))


@app.route("/add_to_stores_wishlist/<store_review_id>")
def add_to_stores_wishlist(store_review_id):
    """
    Update 'wishlist' key of each record
    review with the current session username
    """
    user = mongo.db.users.find_one({"username": session["user"]})
    in_wishlist = mongo.db.store_reviews.find_one(
        {"_id": ObjectId(store_review_id), "wishlist": ObjectId(user["_id"])})

    if not in_wishlist:
        mongo.db.store_reviews.find_one_and_update(
                        {"_id": ObjectId(store_review_id)},
                        {"$addToSet": {"wishlist": ObjectId(user["_id"])}})
        flash("Added to wishlist")

    else:
        flash("Review already in wishlist")
    return redirect(url_for("landing"))


@app.route("/delete_wishlist/<review_id>")
def delete_wishlist(review_id):
    """
    find review and remove user
    from the wishlist array
    """
    user = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.reviews.update({"_id": ObjectId(review_id)},
                            {"$pull": {"wishlist": ObjectId(user["_id"])}})
    flash("Removed from wishlist")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_store_wishlist/<store_review_id>")
def delete_store_wishlist(store_review_id):
    """
    Find review and remove user
    from the wishlist array
    """
    user = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.store_reviews.update({"_id": ObjectId(store_review_id)},
                                  {"$pull": {"wishlist":
                                   ObjectId(user["_id"])}})
    flash("Removed from wishlist")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    """
    Located the review id
    and remove
    """
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review removed")
    return redirect(url_for('landing'))


@app.route("/delete_store_review/<store_review_id>")
def delete_store_review(store_review_id):
    """
    Locate the store review id
    and remove
    """
    mongo.db.store_reviews.remove({"_id": ObjectId(store_review_id)})
    flash("Review removed")
    return redirect(url_for('landing'))


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    """
    Find the user in question on
    the mongodb
    """
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("User removed")
    return redirect(url_for('landing'))


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Allow user to send message to
    admin through mongodb collections
    """
    if request.method == "POST":
        message = {
            "username": session["user"],
            "issue": request.form.get("issue")
        }
        # post issue to 'issues' collections
        mongo.db.issues.insert_one(message)
        flash("Message sent")
        return redirect(url_for('contact'))
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
