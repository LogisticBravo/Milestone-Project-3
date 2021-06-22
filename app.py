import os
import datetime
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
@app.route("/home")
def home():
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "index.html", username=username)
    except Exception:
        return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("new_username").lower()})

        if user_exists:
            flash("Username Not Available (It already exists)")
            return redirect(url_for("signup"))

        newsletter_check = "on" if request.form.get(
            "newsletter_check") else "off"
        signup = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("new_username").lower(),
            "password": generate_password_hash(
                request.form.get("new_password")),
            "tandc": "on",
            "is_admin": "off",
            "newsletter_check": newsletter_check,
            "signup_date": datetime.datetime.utcnow(),
            "last_login": datetime.datetime.utcnow()
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("new_username").lower()
        flash("Sign-up Complete")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user_exists:
            if check_password_hash(
                user_exists["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                if session["user"]:
                    username = mongo.db.users.find_one(
                        {"username": session["user"]})
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return render_template("profile.html", username=username)
            else:
                flash("Incorrect Username and/or Password")
                return redirect(request.referrer)
    return reviews()


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        username = mongo.db.users.find_one({"username": session["user"]})
        my_reviews = list(mongo.db.beans.find(
            {"created_by": session["user"]}))
        return render_template(
            "profile.html", username=username, my_reviews=my_reviews)

    return redirect(url_for("home"))


@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("current_username").lower()})
        username = mongo.db.users.find_one(
            {"username": session["user"]})

        if user_exists and user_exists != username:
            flash("Username Not Available (It already exists)")
            return render_template("profile.html", username=username)
        elif user_exists == username:
            flash("That is already your username!")
            return render_template("profile.html", username=username)
        else:
            mongo.db.users.update_one(
                    {"_id": username["_id"]},
                    {"$set": {"username": request.form.get(
                        "current_username").lower()}}
                )
            flash("Username updated succesffully")
            session["user"] = request.form.get("current_username").lower()
            return profile(username)


@app.route("/logout")
def logout():
    flash("Successfully logged out")
    session.pop("user")
    return redirect(url_for("home"))


@app.route("/reviews", methods=["GET", "POST"])
def reviews():
    beans = list(mongo.db.beans.find())
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "reviews.html", username=username, beans=beans)
    except Exception:
        return render_template("reviews.html", beans=beans)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        bean = {
            "bean_name": request.form.get("bean_name"),
            "bean_roast": request.form.get("bean_roast"),
            "bean_rating": request.form.get("bean_rating"),
            "bean_description": request.form.get("bean_description"),
            "bean_origin": request.form.get("bean_origin"),
            "brew_type": request.form.get("brew_type"),
            "bean_image": request.form.get("bean_image"),
            "affialiate_link": request.form.get("affialiate_link"),
            "created_by": session["user"],
            "created_date": datetime.datetime.utcnow()
        }
        mongo.db.beans.insert_one(bean)
        flash("Review Added!")
        return redirect(url_for("reviews"))


@app.route("/edit_review/<bean_id>", methods=["GET", "POST"])
def edit_review(bean_id):
    beans = mongo.db.beans.find()
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            if request.method == "POST":
                edit = {
                    "bean_name": request.form.get("bean_name"),
                    "bean_roast": request.form.get("bean_roast"),
                    "bean_rating": request.form.get("bean_rating"),
                    "bean_description": request.form.get("bean_description"),
                    "bean_origin": request.form.get("bean_origin"),
                    "brew_type": request.form.get("brew_type"),
                    "bean_image": request.form.get("bean_image"),
                    "affialiate_link": request.form.get("affialiate_link"),
                    "created_by": session["user"],
                    "created_date": datetime.datetime.utcnow()
                }
                mongo.db.beans.update({"_id": ObjectId(bean_id)}, edit)
                flash("Review Updated!")
            bean = mongo.db.beans.find_one({"_id": ObjectId(bean_id)})

            return render_template(
                "reviews.html", bean=bean, username=username, beans=beans)
    except Exception:
        return render_template("reviews.html")


@app.route("/delete_review/<bean_id>")
def delete_review(bean_id):
    mongo.db.beans.remove({"_id": ObjectId(bean_id)})
    flash("Review Deleted")
    return redirect(url_for("reviews"))


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    beans = list(mongo.db.beans.find({"$text": {"$search": query}}))
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "reviews.html", username=username, beans=beans)
    except Exception:
        return render_template("reviews.html", beans=beans)


@app.route("/favourite/<bean_id>")
def favourite(bean_id):
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            bean = mongo.db.beans.find_one(
                {"_id": ObjectId(bean_id)})["bean_name"]
            favourite = {
                    "coffee_id": ObjectId(bean_id),
                    "coffee_name": bean
                }
            mongo.db.users.update_one(
                    {"_id": ObjectId(username["_id"])},
                    {"$push": {"favourites": favourite}}
                )
            return redirect(url_for(
                "reviews", bean=bean, username=username))
    except Exception:
        return render_template("reviews.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
