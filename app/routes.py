from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse

from app.forms import LoginForm
from app.forms import PostForm
from app.forms import RegistrationForm
from app.models import Post
from app.models import User
from . import app


@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    posts = Post.objects.all()
    return render_template("index.html", posts=posts)


@app.route("/posting")
@login_required
def posting():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author_id=current_user.get_id(),
        )
        post.save()
        flash("You public your post!")
        return redirect(url_for("index"))
    return render_template("posting.html", title="Write your post!", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.save()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)


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
        next_paige = request.args.get("next")
        if not next_paige or url_parse(next_paige).netloc != "":
            next_paige = url_for("index")
        return redirect(next_paige)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))
