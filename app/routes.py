from flask import render_template

from . import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Master"}
    posts = [
        {"author": {"username": "Pirate"}, "body": "Are you ready, kids?!"},
        {"author": {"username": "Kids"}, "body": "YES!!!"},
    ]
    return render_template("index.html", user=user, posts=posts)


def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)
