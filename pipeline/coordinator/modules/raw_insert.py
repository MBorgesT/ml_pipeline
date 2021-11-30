from gridfs import GridFS

def run(client, file):
    db = client['raw_data']
    fs = GridFS(db)
    latest_id = fs.put(file)

    db['metadata'].delete_many({})
    db['metadata'].insert_one({'latest_file_id': latest_id})