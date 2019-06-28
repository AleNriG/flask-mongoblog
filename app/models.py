import datetime

from app import db


class User(db.Document):
    email = db.StringField(max_lenght=32, required=True)
    username = db.StringField(max_lenght=64, required=True)
    password_hash = db.StringField(max_lenght=128, required=True)


class Post(db.Document):
    title = db.StringField(max_length=64, required=True)
    content = db.StringField(required=True)
    publication_datetime = db.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    author_id = db.ReferenceField(User)


class Comment(db.Document):
    pass
