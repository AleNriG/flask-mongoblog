from flask import Flask
from flask_mongoengine import MongoEngine

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["MONGODB_SETTINGS"] = {"DB": "my_blog_log"}

db = MongoEngine(app)

from . import routes


if __name__ == "__main__":
    app.run()
