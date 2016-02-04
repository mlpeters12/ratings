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

    email = request.form.get("email")
    password = request.form.get("password")


    user = User.query.filter_by(email=email).first()


    if not user:
        flash("Invalid Credentials")
        return redirect("/login-form")

    if user.password != password:
        flash("Incorrect Password")
        return redirect("/login-form")

    session["user_id"]= user.user_id
    flash("Successfully Logged In")
    return redirect("/login-form")

    # if input_email == email:
    #     if input_password == password:
    #         flash('SUCCESS IS YOURS! LOGIN COMPLETE')
    #     else:
    #         flash('Invalid Credentials, dummy.')

    # else:
    #     new_user = User(email = input_email, password = input_password)
    #     db.session.add(new_user)
    #     db.session.commit()
    #     flash('New Account Created! BITCH')
    # return redirect("/login-form")
            
   



















if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
