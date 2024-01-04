from ..model.user_model import User

def get_user(email):
    user = User.objects(email__exact=email).first().to_json()
    if user:
        return {'success': True, 'user': user}, 200
    return {'success': False, 'message': 'user does not exist'}, 200

def get_all_users():
    return {'success': True, 'users': User.objects.to_json()}, 200