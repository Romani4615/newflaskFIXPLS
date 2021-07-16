from flask import Flask

from config import Config

from .main.routes import main

from .authentication.routes import auth

app = Flask(__name__)

app.register_blueprint(main)

app.register_blueprint(auth)

app.config.from_object(Config)
