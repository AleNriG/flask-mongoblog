import datetime

from flask import url_for

from app import db


class User(db.Document):
    email = db.StringField(max_lenght=32, required=True)
    username = db.StringField(max_lenght=32, required=True)
    password = db.StringField(max_lenght=32, required=True)
