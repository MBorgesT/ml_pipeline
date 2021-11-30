from modules import mongo_client
from gridfs import GridFS


def run(model_id):
    client = mongo_client.get()
    db = client['models']

    latest_id = db.find_one({'_id': model_id})
    fs = GridFS(db)
    file = fs.get(latest_id)
    return 'Model deployed successfully'


