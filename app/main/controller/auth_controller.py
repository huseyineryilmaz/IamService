from flask import request
from flask_restful import Resource
from ..service.user_service import register, login

class Register(Resource):
    def post(self):
        return register(request)

class Login(Resource):
    def get(self):
        return login(request)

