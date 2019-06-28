import datetime

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app import db


class User(db.Document):
    email = db.StringField(max_lenght=32, required=True)
    username = db.StringField(max_lenght=64, required=True)
    password_hash = db.StringField(max_lenght=128, required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Document):
    title = db.StringField(max_length=64, required=True)
    content = db.StringField(required=True)
    publication_datetime = db.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    author_id = db.ReferenceField(User)


class Comment(db.Document):
    title = db.StringField(max_length=64, required=True)
    content = db.StringField(required=True)
    publication_datetime = db.DateTimeField(
        default=datetime.datetime.now, required=True
    )
    post_id = db.ReferenceField(Post)
    author_id = db.ReferenceField(User)
