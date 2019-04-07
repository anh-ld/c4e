import mongoengine

# mongodb://admin:​admin@ds021182.mlab.com​:21182/c4e

host = "ds021182.mlab.com​"
port = 21182
db_name = "c4e"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

connect()

class River(mongoengine.Document):
    name = mongoengine.StringField()
    continent = mongoengine.StringField()
    length = mongoengine.IntField()

db = River.objects()
# list all rivers in Africa
print("Rivers in Africa:")
for river in db:
    if river.continent == "Africa":
        print(river.name)

# list all rivers in S.A with length less than 1000m
print("Rivers in S.A with length less than 1000m:")
for river in db:
    if river.continent == "Africa" and river.length < 1000:
        print(river.name)
