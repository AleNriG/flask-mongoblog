from flask import flash
from flask import redirect
from flask import render_template

from app.forms import LoginForm
from . import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Master"}
    posts = [
        {"author": {"username": "Pirate"}, "body": "Are you ready, kids?!"},
        {"author": {"username": "Kids"}, "body": "YES!!!"},
    ]
    return render_template("index.html", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        return redirect("/index")
    return render_template("login.html", title="Sign In", form=form)
