import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "try-me"
    MONGODB_SETTINGS = {"db": "blog"}
