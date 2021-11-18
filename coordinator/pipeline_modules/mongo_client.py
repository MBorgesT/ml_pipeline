import pymongo

#MONGO_URL = 'mongodb://mongo/'
MONGO_URL = 'mongodb://localhost:5002/'

def get():
    return pymongo.MongoClient(MONGO_URL, username='root', password='root')