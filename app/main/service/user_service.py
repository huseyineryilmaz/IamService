from ..model.user_model import User

def get_user(email):
    user = User.objects(email=email).to_json()
    if user:
        return {'success': True, 'user': user}
    return {'success': False, 'message': 'user does not exist'}

def get_all_users():
    return {'success': True, 'users': User.objects.to_json()}