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


# Basic C.R.U.D functionality adapted from CI Task Manager walkthrough Project.
@app.route("/")
@app.route("/home")
def home():
    reviews = list(mongo.db.beans.aggregate([{
        "$sort": {"created_date": -1}}, {"$limit": 5}]))
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "index.html", username=username, reviews=reviews)
    except Exception:
        return render_template("index.html", reviews=reviews)


# creates a new user in the DB. Assings default value of false for is_admin.
# Set's up favourite array for later use when favouriting reviews.
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("new_username").lower()})

        if user_exists:
            flash("Username Not Available (It already exists)")
            return redirect(url_for("signup"))

        newsletter_check = "checked" if request.form.get(
            "newsletter_check") else "off"
        fav = [{"fav_id": ObjectId(), "favshown": False}]
        signup = {
            "email": request.form.get("email").lower(),
            "username": request.form.get("new_username").lower(),
            "password": generate_password_hash(
                request.form.get("new_password")),
            "tandc": "on",
            "is_admin": False,
            "newsletter_check": newsletter_check,
            "signup_date": datetime.datetime.utcnow(),
            "last_login": datetime.datetime.utcnow(),
            "favourites": fav
        }
        mongo.db.users.insert_one(signup)

        session["user"] = request.form.get("new_username").lower()
        flash("Sign-up Complete")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


# Basic Authentication and session.
# Adapted from CI course Task Manager walkthrough module.
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
                    return profile(username)
            else:
                flash("Incorrect Username and/or Password")
                return redirect(request.referrer)
    return reviews()


# Lists users reviews that they have created and
# reviews that they have favourited.
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            my_reviews = list(mongo.db.beans.find(
                {"created_by_id": username["_id"]}))
            favourites = list(mongo.db.beans.find(
                {"favoured_by": {"$elemMatch": {
                    "username": username["username"]}}}
            ))
            return render_template(
                "profile.html", username=username,
                my_reviews=my_reviews, favourites=favourites)
    except Exception:
        return redirect(url_for("home"))


# Allows the user to update their username.
# Check's if it exists or if it's their current username.
# Check's password authentication of change before submission to the DB.
@app.route("/update", methods=["GET", "POST"])
def update():
    if request.method == "POST":
        user_exists = mongo.db.users.find_one(
            {"username": request.form.get("current_username").lower()})
        username = mongo.db.users.find_one(
            {"username": session["user"]})

        if user_exists and user_exists != username:
            if check_password_hash(
                    user_exists["password"], request.form.get(
                        "current_password")):
                flash("Username Not Available (It already exists)")
                return render_template("profile.html", username=username)
            else:
                flash("Incorrect Password")
                return render_template("profile.html", username=username)
        elif user_exists == username:
            if check_password_hash(
                    user_exists["password"], request.form.get(
                        "current_password")):
                flash("That is already your username!")
                return render_template("profile.html", username=username)
            else:
                flash("Incorrect Password")
                return render_template("profile.html", username=username)
        else:
            if check_password_hash(
                username["password"], request.form.get(
                    "current_password")):
                mongo.db.users.update_one(
                    {"_id": username["_id"]},
                    {"$set": {"username": request.form.get(
                        "current_username").lower()}}
                )
                mongo.db.beans.update_many(
                    {"created_by_id": username["_id"]},
                    {"$set": {"created_by": request.form.get(
                        "current_username").lower()}}
                )
            else:
                flash("Incorrect Password")
                return render_template("profile.html", username=username)
            flash("Username updated succesffully")
            session["user"] = request.form.get("current_username").lower()
            return profile(username)


# Allows user to update their password to a new one.
# Check's if the password is their current password.
@app.route("/update_pw", methods=["GET", "POST"])
def update_pw():
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    if request.method == "POST":
        if session["user"]:
            if check_password_hash(
                username["password"], request.form.get(
                    "new_password")):
                flash("That's already your password!")
            else:
                mongo.db.users.update_one(
                    {"_id": username["_id"]},
                    {"$set": {"password": generate_password_hash(
                        request.form.get("new_password"))}})
                flash("Password Updated Successfully!")
            return profile(username)


# Updates user's subscription preferences to the newsletter from their profile.
@app.route("/newsletter_sub", methods=["GET", "POST"])
def newsletter_sub():
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    newsletter_check = "checked" if request.form.get(
        "subscription") else "off"
    if request.method == "POST":
        if session["user"]:
            mongo.db.users.update_one(
                {"_id": username["_id"]},
                {"$set": {"newsletter_check": newsletter_check}})
        return profile(username)


# Updates users subscription preferences to the newsletter if they
# subscribe via the newsletter pop-up modal via the reviews.html page.
# Add's the users name and email address to a database if they're not logged in
# or are not a user.
# Allows collection of name's and emails for future targeting.
@app.route("/newsletter_form", methods=["GET", "POST"])
def newsletter_form():
    if request.method == "POST":
        try:
            if session["user"]:
                username = mongo.db.users.find_one(
                    {"username": session["user"]})
                newsletter_check = "checked" if request.form.get(
                    "newsletterSub") else "off"
                mongo.db.users.update_one(
                    {"_id": username["_id"]},
                    {"$set": {"newsletter_check": newsletter_check}})
                flash("Thanks for updating your Subscription!")
                return reviews()
        except Exception:
            newsletter = {
                "name": request.form.get("user_name"),
                "email": request.form.get("user_email")
            }
            mongo.db.newsletters.insert_one(newsletter)
            flash("Thanks for subscribing! Why not Create an Account?")
            return render_template("signup.html")


# logout the user and ends the session.
@app.route("/logout")
def logout():
    try:
        if session["user"]:
            username = mongo.db.users.find_one(
                    {"username": session["user"]})
            mongo.db.users.update_one(
                    {"_id": username["_id"]},
                    {"$set": {"last_login": datetime.datetime.utcnow()}})
            flash("Successfully logged out")
            session.pop("user")
        return home()
    except Exception:
        return home()


# lists the reviews on the review.html page.
# Also set's reviews that are already
# favourited by the user on the respective reviews.
@app.route("/reviews", methods=["GET", "POST"])
def reviews():
    origins = list(mongo.db.origin.find().sort("origin_type", 1))
    roasts = list(mongo.db.roast.find())
    beans = list(mongo.db.beans.find())
    username = mongo.db.users.find_one({"username": session})
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            favourites = list(username["favourites"])
            return render_template(
                "reviews.html", username=username,
                beans=beans, origins=origins,
                favourites=favourites, roasts=roasts)
    except Exception:
        return render_template("reviews.html", beans=beans, username=username)


# Inserts the review to the database.
@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        username = mongo.db.users.find_one({"username": session["user"]})
        bean = {
            "bean_name": request.form.get("bean_name"),
            "bean_roast": request.form.get("bean_roast"),
            "bean_rating": request.form.get("bean_rating"),
            "bean_description": request.form.get("bean_description"),
            "bean_origin": request.form.get("bean_origin"),
            "brew_type": request.form.get("brew_type"),
            "origin_type": request.form.get("origin_type"),
            "bean_image": request.form.get("bean_image"),
            "affialiate_link": request.form.get("affialiate_link"),
            "created_by": session["user"],
            "created_by_id": username["_id"],
            "created_date": datetime.datetime.utcnow(),
            "favshown": True
        }
        mongo.db.beans.insert_one(bean)
        flash("Review Added!")
        return reviews()


# Allows the user to edit reviews which they have written.
# Admin can also edit reviews.
@app.route("/edit_review/<bean_id>", methods=["GET", "POST"])
def edit_review(bean_id):
    beans = mongo.db.beans.find()
    username = mongo.db.users.find_one({"username": session["user"]})
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            if request.method == "POST":
                mongo.db.beans.update_one({"_id": ObjectId(bean_id)}, {
                    "$set": {"bean_name": request.form.get("bean_name"),
                             "bean_roast": request.form.get("bean_roast"),
                             "bean_description": request.form.get(
                                 "bean_description"),
                             "bean_origin": request.form.get("bean_origin"),
                             "origin_type": request.form.get("origin_type"),
                             "brew_type": request.form.get("brew_type"),
                             "bean_image": request.form.get("bean_image"),
                             "affialiate_link": request.form.get(
                                 "affialiate_link"),
                             "created_by": session["user"],
                             "created_date": datetime.datetime.utcnow()}})
                flash("Review Updated!")
            return render_template("reviews.html",
                                   username=username, beans=beans)
    except Exception:
        return reviews()


# Deletes the review from the database. Admin can also delete reviews.
@app.route("/delete_review/<bean_id>")
def delete_review(bean_id):
    mongo.db.beans.delete_one({"_id": ObjectId(bean_id)})
    flash("Review Deleted")
    return reviews()


# Add's a comment to a comment array within each review document.
# Give's the comment a unique id and ties the comment to the user
# that left it via username and their unique ObjectId.
@app.route("/add_comment/<bean_id>", methods=["GET", "POST"])
def add_comment(bean_id):
    if session["user"]:
        username = mongo.db.users.find_one({"username": session["user"]})
        if request.method == "POST":
            comments = {
                "comment_id": ObjectId(),
                "user_id": username["_id"],
                "username": username["username"],
                "comment": request.form.get("comment")
            }
            mongo.db.beans.update_one(
                {"_id": ObjectId(bean_id)},
                {"$push": {"comments": comments}})
            flash("Added Comment!")
        return reviews()


# Removes a comment from the database if the user wrote it.
# Admin can also delete comments.
@app.route("/delete_comment/<bean_id>/<comment_id>")
def delete_comment(bean_id, comment_id):
    if session["user"]:
        mongo.db.beans.update_one(
            {"_id": ObjectId(bean_id)},
            {"$pull": {"comments": {"comment_id": ObjectId(comment_id)}}}
        )
        flash("comment removed")
    return reviews()


# Searches the database and lsits the results.
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    beans = list(mongo.db.beans.find({"$text": {"$search": query}}))
    username = "user"
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            return render_template(
                "reviews.html", username=username, beans=beans)
        else:
            return render_template("reviews.html", beans=beans)
    except Exception:
        return render_template("reviews.html", beans=beans, username=username)


# Allows for a user to favourite a review. Updates both the review (beans)
# document aswell as the users document with who has favourited it and
# what reviews a user has favourited.
# Updating both allows for future reporting on the number of reviews
# favourited by a user and the number of favourites a review has.
@app.route("/favourite/<bean_id>")
def favourite(bean_id):
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            bean = mongo.db.beans.find_one(
                {"_id": ObjectId(bean_id)})["bean_name"]
            favourite = {
                "coffee_id": ObjectId(bean_id),
                "coffee_name": bean,
                "favshown": True
            }
            mongo.db.users.update_one(
                {"_id": ObjectId(username["_id"])},
                {"$push": {"favourites": favourite}}
            )
            mongo.db.beans.update_one(
                {"_id": ObjectId(bean_id)},
                {"$push": {"favoured_by": {
                    "user_id": username["_id"],
                    "username": username["username"]}}}
            )
            flash("Added to your Favourites!")
            return reviews()
    except Exception:
        return render_template("reviews.html")


# Removes a favourited review from both the user and review (beans) document.
@app.route("/remove_favourite/<bean_id>")
def remove_favourite(bean_id):
    if session["user"]:
        username = mongo.db.users.find_one({"username": session["user"]})
        mongo.db.beans.update_one(
            {"_id": ObjectId(bean_id)},
            {"$pull": {"favoured_by": {"user_id": username["_id"]}}}
        )
        mongo.db.users.update_one(
            {"_id": ObjectId(username["_id"])},
            {"$pull": {"favourites": {"coffee_id": ObjectId(bean_id)}}}
        )
        flash("Yikes! Left a bad taste?!")
    return reviews()


# App route for the contact page.
@app.route("/contact")
def contact():
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            return render_template("contact.html", username=username)
    except Exception:
        return render_template("contact.html")


# App route for the privacy policy. The policy is stored in the DB and
# jinja templating is used to create the privacy policy page.
@app.route("/privacy")
def privacy():
    privacy_policy = mongo.db.privacy_policy.find()
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            privacy_policy = mongo.db.privacy_policy.find()
            return render_template("privacy.html",
                                   privacy_policy=privacy_policy,
                                   username=username)
    except Exception:
        return render_template("privacy.html", privacy_policy=privacy_policy)


# App route for the admin page. Only visible to admins.
# Lists basic stats of the site and user preferences such as
# newseltter subscription status and if they are an admin or not.
@app.route("/admin")
def admin():
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
            if username["is_admin"] is True:
                users = list(mongo.db.users.find())
                beans = list(mongo.db.beans.find())
                return render_template("admin.html", username=username,
                                       users=users, beans=beans)
            else:
                flash("Unauthorized")
                return home()
    except Exception:
        return home()


# Allows for an admin to delete an account from the database.
@app.route("/delete_account/<user_id>")
def delete_account(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    flash("Account Deleted")
    return admin()


# Allows the site owner or admins to enable other users with admin permissions.
@app.route("/enable_admin/<user_id>")
def enable_admin(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user["is_admin"] is False:
        mongo.db.users.update_one(
            {"_id": user["_id"]},
            {"$set": {"is_admin": True}})
    else:
        mongo.db.users.update_one(
            {"_id": user["_id"]},
            {"$set": {"is_admin": False}})
    flash("Permission Updated")
    return admin()


# Error handling for 404. note that 404 status set explicitly.
# adapted from flask documentation:
# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    try:
        if session["user"]:
            username = mongo.db.users.find_one({"username": session["user"]})
        return render_template('404.html', username=username), 404
    except Exception:
        return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
