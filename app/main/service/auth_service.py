
from ..model.user_model import User
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
        return {'success': False, 'Exception': e.args}
    return {'success': True, 'message': 'User created.'}

def login(request):
    try:
        data = request.get_json()
        email = data['email']
        password = data['password'].encode('utf-8')
        user = User.objects(email=email)
        if user and bcrypt.checkpw(password, user.password.encode('utf-8')):
            return {'success': True, 'message': 'Login succeed.'}
        else:
            return {'success': False, 'message': 'Login failed.'}
    except Exception as e:
        return {'success': False, 'Exception': e.args}
def refresh():
    current_user = get_jwt_identity()
    return {'access_token': create_access_token(identity=current_user)}, 200

def protected():
    current_user = get_jwt_identity()
    return {'logged_in_as': current_user}, 200