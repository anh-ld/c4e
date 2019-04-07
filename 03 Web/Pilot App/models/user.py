from mongoengine import *

class User(Document):
    name = StringField()
    email = StringField()
    username = StringField()
    password = StringField()
