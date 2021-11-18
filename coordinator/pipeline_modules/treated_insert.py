import json

def run(client, df):
    db = client['treated_data']
    data_collection = db['data']

    data_json = json.loads(df.to_json(orient='records'))
    data_collection.insert_many(data_json)