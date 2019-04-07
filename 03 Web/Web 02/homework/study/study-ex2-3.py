import mlab
import json
from mongoengine import *

# design database
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() # 0: female, 1: male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

mlab.connect()
id_to_find = "5ac09495b99c7f2e2ff0bf48"

# finding document based on id
doc = Service.objects(id = id_to_find)
print("Document found:",json.loads(doc.to_json()))

# delete the document found
# doc.delete()
