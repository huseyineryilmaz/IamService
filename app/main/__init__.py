from flask import Flask
from mongoengine import connect
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .controller.auth_controller import Register, Login, Refresh, Protected
from .controller.user_controller import UserList, User
from .config import DATABASE_URI, FLASK_DEBUG, SECRET_KEY, JWT_SECRET_KEY

def create_app():
    connect(host=DATABASE_URI)
    app = Flask(__name__)
    app.debug = FLASK_DEBUG
    app.secret_key = SECRET_KEY
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    jwt = JWTManager(app)
    api = Api(app)
    api.add_resource(Register, '/auth/register')
    api.add_resource(Login, '/auth/login')
    api.add_resource(UserList, '/userlist')
    api.add_resource(User, '/user/<email>')
    api.add_resource(Refresh, '/refresh')
    api.add_resource(Protected, '/protected')
    return app