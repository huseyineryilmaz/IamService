
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
        for user in User.objects(email=email):
            if bcrypt.checkpw(password, user.password.encode('utf-8')):
                return {'success': True, 'message': 'Login succeed.'}
            else:
                return {'success': False, 'message': 'Login failed.'}
        return {'success': False, 'message': 'Login failed.'}
    except Exception as e:
        return {'success': False, 'Exception': e.args}