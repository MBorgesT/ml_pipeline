from pipeline_modules import mongo_client, raw_insert, etl, treated_insert, train_model

def pipeline(file):
    client = mongo_client.get()

    raw_insert.run(client, file)
    df = etl.run(client)
    treated_insert.run(client, df)
    train_model.run(df)
