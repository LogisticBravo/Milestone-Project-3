import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_coffee")
def get_beans():
    beans = mongo.db.beans.find()
    return render_template("coffee.html", beans=beans)


@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/reviews", methods=["GET", "POST"])
def reviews():
    beans = mongo.db.beans.find()
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
            "affialiate_link": request.form.get("affialiate_link")
        }
        mongo.db.beans.insert_one(bean)
        return redirect(url_for("reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
