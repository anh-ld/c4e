from pymongo import MongoClient

# database -> collection -> document

mongo_uri = "mongodb://admin:admin@ds117749.mlab.com:17749/c4e16-db"
# connect to database
client = MongoClient(mongo_uri)
# get database
db = client.get_default_database()
# create collection
animals = db["animals"]
# animals_list = ["Dog","Fox","Mouse","Ox","Horse","Bird","Eagle"]
# # create a new document
# for i in range(len(animals_list)):
#     new_animal = {
#         "name" : animals_list[i],
#         "description" : "A human's friend"
#     }
# # insert document to collection
#
#     animals.insert_one(new_animal)

all_animals = animals.find()
for animal in all_animals:
    print(animal["name"])
