from ..model.user_model import User
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
import bcrypt

def register(request):
    try:
        data = request.get_json()
        email = data['email']
        first_name = data['firstname']
        last_name = data['lastname']
        password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        new_user = User(email=email, first_name=first_name, last_name=last_name, password=password)
        new_user.save()
    except Exception as e:
        return {'success': False, 'Exception': e.args}, 400
    return {'success': True, 'message': 'User created.'}, 200

def login(request):
    try:
        data = request.get_json()
        email = data['email']
        password = data['password'].encode('utf-8')
        login_user = User.objects(email__exact=email)
        if login_user and bcrypt.checkpw(password, login_user.first().password.encode('utf-8')):
            return {'success': True,
                    'message': 'Login succeed.',
                    'access_token': create_access_token(identity=email),
                    'refresh_token': create_refresh_token(identity=email)
                }, 200
        else:
            return {'success': False, 'message': 'Login failed.'}, 401
    except Exception as e:
        return {'success': False, 'Exception': e.args}, 401

def refresh():
    current_user = get_jwt_identity()
    return {'access_token': create_access_token(identity=current_user)}, 200

def protected():
    current_user = get_jwt_identity()
    return {'logged_in_as': current_user}, 200