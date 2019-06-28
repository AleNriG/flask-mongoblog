from flask import Flask
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine(app)
login = LoginManager(app)
login.login_view = "login"

from . import routes


if __name__ == "__main__":
    app.run()
