from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_login import current_user
from flask_login import login_user

from . import app
from app.forms import LoginForm
from app.models import User


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
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
