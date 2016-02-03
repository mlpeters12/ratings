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


@app.route("/profile-page", methods=["POST"])
def process_login():

    input_email = request.form.get("email")
    input_password = request.form.get("password")

    user_information = User.query.(User.id, User.email, User.password).all()


    for user in user table:
        if username == username:
            if password == password:
                return render_template(profilepage.html)
            else:
                return alert
        else:
            create new username in database and db.session.commit()
            return render_template(profilepage.html)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
