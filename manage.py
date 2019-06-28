from flask_script import Manager
from flask_script import Server

from app import app

manager = Manager(app)

manager.add_command("runserver", Server(use_debugger=True, use_reloader=True))

if __name__ == "__main__":
    manager.run()
