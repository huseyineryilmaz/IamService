from flask import request
from flask_restful import Resource
from ..model.user_model import UserModel

class User(Resource):
    def get(self):
        return {'success': True}
    def post(self):
        try:
            data = request.get_json()
            email = data['email']
            first_name = data['firstname']
            last_name = data['lastname']
            new_user = UserModel(email=email, first_name=first_name, last_name=last_name)
            new_user.save()
        except Exception as e:
            print('Error is ************************************************** ', e)
            return e
        return {'success': True}