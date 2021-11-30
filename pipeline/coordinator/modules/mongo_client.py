import pymongo

MONGO_URL = 'mongodb://mongo/'

def get():
    return pymongo.MongoClient(MONGO_URL, username='root', password='root')