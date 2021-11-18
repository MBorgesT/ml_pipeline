from tensorflow import keras
from tensorflow.keras import layers

import mlflow
import mlflow.keras

DEBUG = True

if DEBUG:
    WORKING_DIR = '/home/matheus/IC/pipeline'
else:
    WORKING_DIR = '/usr/src'
MODEL_PATH = WORKING_DIR + '/coordinator/pipeline_modules/ml/model.h5'


def get_model(input_shape, dropout=.18):
    model =  keras.Sequential([
        layers.Dense(256, activation='relu', input_shape=[input_shape]), layers.Dropout(dropout),
        layers.Dense(256, activation='relu'), layers.Dropout(dropout),
        layers.Dense(128, activation='relu'), layers.Dropout(dropout),
        layers.Dense(64, activation='relu'), layers.Dropout(dropout),
        layers.Dense(32, activation='relu'),
        layers.Dense(1),
    ])

    optimizer = keras.optimizers.RMSprop(.001)


    model.compile(
        loss='mse',
        optimizer=optimizer,
        metrics=['mae', 'mse']
    )

    return model


def train_model(X, y, n_epochs=10, batch_size=32):
    with mlflow.start_run() as run:
        try:
            model = keras.models.load_model(MODEL_PATH)
        except:
            model = get_model(X.shape[1])
        
        history = model.fit(
            X, y, epochs=n_epochs, batch_size=batch_size,
            validation_split=.2, verbose=1
        )

        for key, value in history.history.items():
            mlflow.log_metric(key, value[-1])
        mlflow.keras.log_model(model, 'keras')

        model.save(MODEL_PATH)

        return history