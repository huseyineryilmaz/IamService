from mongoengine import Document, EmailField, StringField

class UserModel(Document):
    email = EmailField(required=True, unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    meta={'collection': 'user'}
    def _init__(self, email, first_name, last_name):
        self.email=email,
        self.first_name=first_name
        self.last_name=last_name
