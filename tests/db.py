import pymongo
from gridfs import GridFS

from datetime import datetime

file_path = 'FRA3-FRA6_cleaned_feature_engineered.csv'
file = open(file_path, 'rb')

MONGO_URL = 'mongodb://localhost:5001/'

client = pymongo.MongoClient(MONGO_URL, username='root', password='root')
db = client['csv_files']
fs = GridFS(db)
latest_id = fs.put(file)

db['metadata'].delete_many({})
db['metadata'].insert_one({'latest_file_id': latest_id})