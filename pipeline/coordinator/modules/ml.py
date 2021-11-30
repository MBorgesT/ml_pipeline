import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from tensorflow import keras
from tensorflow.keras import layers

from . import mongo_client

from aim import Run

from gridfs import GridFS


def get_model(input_shape, dropout, lr):
    model = keras.Sequential([
        layers.Dense(256, activation='relu', input_shape=[input_shape]), layers.Dropout(dropout),
        layers.Dense(256, activation='relu'), layers.Dropout(dropout),
        layers.Dense(128, activation='relu'), layers.Dropout(dropout),
        layers.Dense(64, activation='relu'), layers.Dropout(dropout),
        layers.Dense(32, activation='relu'),
        layers.Dense(1),
    ])
    model.compile(
        loss='mse',
        optimizer=keras.optimizers.RMSprop(lr),
        metrics=['mae', 'mse']
    )

    return model


def save_model_to_db(model):
    model.save('temp.h5')
    with open('temp.h5', 'rb') as f:
        client = mongo_client.get()
        db = client['models']
        fs = GridFS(db)
        inserted_id = fs.put(f)
    
    os.remove('temp.h5')
    return inserted_id


def train_model(X, y, n_epochs=5, batch_size=32, dropout=0.18, lr=.01):
    run = Run()

    model = get_model(X.shape[1], dropout, lr)
        
    history = model.fit(
        X, y, epochs=n_epochs, batch_size=batch_size,
        validation_split=.2, verbose=1
    )

    model_id = save_model_to_db(model)
    print('\n\n\n\n\n')
    print(model_id)
    print('\n\n')
    print(type(model_id))
    print('\n\n\n\n\n')
    
    run['hparams'] = {
        'model_id': str(model_id),
        'lr': lr,
        'dropout': dropout
    }

    for key, values in history.history.items():
        for i, v in enumerate(values):
            run.track(v, name=key, step=i)

    return history