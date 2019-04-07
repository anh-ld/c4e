import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds237989.mlab.com:37989/cmsapp

host = "ds237989.mlab.com"
port = 37989
db_name = "cmsapp"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
