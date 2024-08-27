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
def home():
    return render_template("index.html")


@app.route("/get_rides")
def get_rides():
    rides = mongo.db.rides.find()
    return render_template("rides.html", rides=rides)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == 'POST':
        reviews = {
            "created_by": session["user"],
            "name" : request.form.get("name"),
            "ride" : request.form.get("ride"),
            "theme_park": request.form.get("theme_park"),
            "rating": request.form.get("rating"),
            "ride_comment": request.form.get("ride_comment"),
            "other_comment": request.form.get("other_comment")
        }
        
        mongo.db.reviews.insert_one(reviews)
        flash("Review Successfully Added!")
        return redirect(url_for("add_review"))

    rides = mongo.db.rides.find().sort("ride_name", 1)
    return render_template("add_review.html")


@app.route("/reviews", methods=["GET","POST"])
def get_reviews():
    reviews = mongo.db.reviews.find()
    return render_template("reviews.html", reviews=reviews)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == 'POST':
        submit = {
            "created_by": session["user"],
            "name" : request.form.get("name"),
            "ride" : request.form.get("ride"),
            "theme_park": request.form.get("theme_park"),
            "rating": request.form.get("rating"),
            "ride_comment": request.form.get("ride_comment"),
            "other_comment": request.form.get("other_comment")
        }
        
        mongo.db.reviews.update_one({"_id": ObjectId(review_id)}, {"$set": submit})
        flash("Review Successfully Updated!")
        
    reviews = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    return render_template("edit_review.html", reviews=reviews)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.delete_one({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted!")
    return redirect(url_for("get_reviews"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("register"))
        
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user in a 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username = session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username = session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)