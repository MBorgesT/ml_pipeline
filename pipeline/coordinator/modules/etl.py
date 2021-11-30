from gridfs import GridFS
import pandas as pd


def run(client):
    # datasets already treated, so just gonna return it as a dataframe
    db = client['raw_data']

    latest_id = db['metadata'].find_one({})['latest_file_id']
    fs = GridFS(db)
    csv = fs.get(latest_id)

    return pd.read_csv(csv)
