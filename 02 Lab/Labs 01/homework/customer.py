from pymongo import MongoClient
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
customers = db["customers"]

wom = customers.find({"ref":"wom"}).count()
ads = customers.find({"ref":"ads"}).count()
events = customers.find({"ref":"events"}).count()

print("Number of customers group by refs")
print("wom: {}, ads: {}, events: {}".format(wom,ads,events))

labels = ["Word of Mouth","Advertisements","Events"]
values = [wom, ads, events]
colors = ["purple","green","orange"]

pyplot.pie(values, labels=labels,colors=colors,autopct="%.2f%%",shadow=True)
pyplot.axis("equal")

pyplot.show()
