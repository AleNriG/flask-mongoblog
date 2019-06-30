import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "try-me"
    MONGODB_SETTINGS = {
        "db": os.environ.get("DB_NAME"),
        "host": os.environ.get("MONGO_URL"),
        "username": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASS")
    }
