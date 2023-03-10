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
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_books")
def get_books():
    books = list(mongo.db.booksread.find())
    return render_template("readinglist.html", booksread=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please choose a different name")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    books = list(mongo.db.booksread.find())
    unread = list(mongo.db.bookstoberead.find())
    categories = mongo.db.reading_list.find().sort("category_name", 1)

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html",
            username=username, booksread=books, bookstoberead=unread, reading_list=categories
            )

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "rating": request.form.get("rating"),
            "release_date": request.form.get("release_date"),
            "publisher": request.form.get("publisher"),
            "page_count": request.form.get("page_count"),
            "isbn": request.form.get("isbn")
            }
        mongo.db.bookstoberead.insert_one(book)

        flash("Book Successfully Added")
        return redirect(url_for("add_book"))

    bookcat = mongo.db.reading_list.find().sort("category_name", 1)
    return render_template("add_book.html", reading_list=bookcat)


@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "rating": request.form.get("rating"),
            "release_date": request.form.get("release_date"),
            "publisher": request.form.get("publisher"),
            "page_count": request.form.get("page_count"),
            "isbn": request.form.get("isbn")
        }
        mongo.db.tasks.update({"_id": ObjectId(book_id)}, submit)
        flash("Book Entry Edited")

    books = mongo.db.booksread.find_one({"_id": ObjectId(book_id)})
    categories = mongo.db.reading_list.find().sort("category_name", 1)
    return render_template(
        "profile.html", booksread=books, readinglist=categories
        )


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
