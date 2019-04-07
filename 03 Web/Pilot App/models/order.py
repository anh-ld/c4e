from mongoengine import *
from .service import Service
from .user import User

class Order(Document):
    service_id = ReferenceField(Service)
    user_id = ReferenceField(User)
    time = StringField()
    is_accepted = BooleanField()
