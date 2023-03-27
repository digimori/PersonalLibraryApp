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
            "isbn": request.form.get("isbn"),
            "synopsis": request.form.get("synopsis")
        }

        book = mongo.db.booksread.find_one({"_id": ObjectId(book_id)})
        mongo.db.booksread.replace_one({"_id": ObjectId(book_id)}, submit)
        flash("Book Entry Edited")
    return redirect(url_for("profile", username=session["user"]))

    categories = mongo.db.reading_list.find().sort("category_name", 1)
    return render_template(
        "profile.html", booksread=booksread,
        reading_list=categories, username=session["user"]
        )


@app.route("/search", methods=["GET", "POST"])
def search():
    categories = mongo.db.reading_list.find().sort("category_name", 1)
    query = request.form.get("query")
    booksread = list(mongo.db.booksread.find({"$text": {"$search": query}}))

    return render_template(
        "profile.html", username=session["user"],
        booksread=booksread, reading_list=categories
        )


# ---------------- REGISTRATION AND LOGIN/LOGOUT FUNCTIONS -------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
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


# ------------------------ MAIN PROFILE PAGE ------------------------


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    books = list(mongo.db.booksread.find())
    categories = list(mongo.db.reading_list.find().sort("category_name", 1))

    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template(
            "profile.html",
            username=username, booksread=books,
            reading_list=categories
            )

    return redirect(url_for("login", username=session["user"]))


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("index"))


# ------------------------ ADDING AND EDITING BOOKS ------------------------

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
            "isbn": request.form.get("isbn"),
            "synopsis": request.form.get("synopsis"),
            "bookimg": request.form.get("bookimg")
            }
        mongo.db.booksread.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("add_book"))

    bookcat = mongo.db.reading_list.find().sort("category_name", 1)
    return render_template(
        "add_book.html", reading_list=bookcat, username=session["user"])


@app.route("/profile/<username>, <book_id>", methods=["GET", "POST"])
def edit_book(username, book_id):
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
            "isbn": request.form.get("isbn"),
            "synopsis": request.form.get("synopsis"),
            "bookimg": request.form.get("bookimg")
        }

        book = mongo.db.booksread.find({"_id": ObjectId(book_id)}, submit)
        mongo.db.booksread.replace_one(
            {"_id": ObjectId(book_id)}, submit, True)
        categories = mongo.db.reading_list.find().sort("category_name", 1)
        flash("Book Entry Edited")
    return redirect(url_for("profile", username=session["user"]))

    return render_template(
        "profile.html",
        book=book, reading_list=categories, username=session["user"]
        )


@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    mongo.db.booksread.delete_one({"_id": ObjectId(book_id)})
    flash("Book Entry Successfully Deleted")
    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
