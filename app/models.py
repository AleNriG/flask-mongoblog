from app import db


class User(db.Document):
    email = db.StringField(max_lenght=32, required=True)
    username = db.StringField(max_lenght=64, required=True)
    password_hash = db.StringField(max_lenght=128, required=True)
