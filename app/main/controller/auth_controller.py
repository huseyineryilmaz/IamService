from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from ..service.auth_service import register, login, refresh, protected

class Register(Resource):
    def post(self):
        return register(request)

class Login(Resource):
    def get(self):
        return login(request)

class Refresh(Resource):
    @jwt_required(refresh=True)
    def get(self):
        return refresh()


class Protected(Resource):
    @jwt_required()
    def get(self):
        return protected()