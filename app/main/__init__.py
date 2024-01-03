from flask import Flask
from mongoengine import connect
from flask_restful import Api
from .controller.auth_controller import Register, Login
from .controller.user_controller import UserList, User
from .config import DATABASE_URI, FLASK_DEBUG, SECRET_KEY

def create_app():
    connect(host=DATABASE_URI)
    app = Flask(__name__)
    app.debug = FLASK_DEBUG
    app.secret_key = SECRET_KEY
    api = Api(app)
    api.add_resource(Register, '/auth/register')
    api.add_resource(Login, '/auth/login')
    api.add_resource(UserList, '/userlist')
    api.add_resource(User, '/user/<email>')
    return app