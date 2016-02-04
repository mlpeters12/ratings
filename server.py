"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "marvelpie"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""

    return render_template("homepage.html")

@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/login-form")
def login_form():
    """Shows the login form"""

    return render_template("login_form.html")


@app.route("/login-form", methods=["POST"])
def process_login():
    """processes login info"""

    email = request.form.get("email")
    password = request.form.get("password")


    user = User.query.filter_by(email=email).first()


    if not user:
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("New user logged in!")
        return redirect("/")

    if user.password != password:
        flash("Incorrect Password")
        return redirect("/login-form")

    session["user_id"]= user.user_id
    flash("Successfully Logged In")
    return redirect("/")


@app.route("/logout")
def logout():
    """logs user out"""
    
    del session["user_id"]        
    flash("You're logged out, loser.")
    return redirect("/")

@app.route("/users/<int:user_id>", methods=["GET"])
def user_page(user_id):
    """Show user page"""

    user_info = db.session.query(User,
                                Rating).join(Rating).all()
    # movie_info = db.session.query(Rating,
    #                                 Movie).join(Movie).all()

    for user, rating in user_info:
        print user_id, user.age, user.zipcode

    # for rating, movie in movie_info:
        # print rating.score, movie.title

    # return render_template("user_list.html", users=users)
   



















if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
