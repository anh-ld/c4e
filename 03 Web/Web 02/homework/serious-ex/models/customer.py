from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField() # 0: female, 1: male
    email = StringField()
    phone = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
