from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
db = client.get_default_database()
blog = db["posts"]

post = {
    "title" : "Ai đưa em về",
    "author" : "Duy Anh",
    "content" : """
    Đêm nay ai đưa em về
    Đường khuya sao trời lấp lánh
    Đêm nay ai đưa em về
    Mắt em sao chiếu long lanh
    """
}
blog.insert_one(post)
