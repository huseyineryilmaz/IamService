from flask import request
from flask_restful import Resource
from ..service.user_service import get_user, get_all_users

class UserList(Resource):
    def get(self):
        return get_all_users()

class User(Resource):
    def get(self, email):
        return get_user(email)
