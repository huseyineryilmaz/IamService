from flask import Flask
from mongoengine import connect
from flask_restful import Api
from ..main.controller.user_controller import User
from .config import DATABASE_URI, FLASK_DEBUG, SECRET_KEY

def create_app():
    connect(host=DATABASE_URI)
    app = Flask(__name__)
    app.debug = FLASK_DEBUG
    app.secret_key = SECRET_KEY
    api = Api(app)
    api.add_resource(User, '/')
    return app