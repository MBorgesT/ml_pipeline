import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

from tensorflow import keras
from tensorflow.keras import layers

import mlflow
import mlflow.keras
mlflow.set_tracking_uri('http://mlflow-server:5000/')
#mlflow.set_tracking_uri('http://localhost:5004/')
mlflow.set_experiment('default')

print('tracking uri:', mlflow.get_tracking_uri())
print('artifact uri:', mlflow.get_artifact_uri())


from datetime import datetime
import os


WORKING_DIR = os.environ['WORKDIRPATH']
MODEL_PATH = WORKING_DIR + '/coordinator/'


def get_model(input_shape, dropout=.18, lr=.001):
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


def train_model(X, y, n_epochs=5, batch_size=32):
    try:
        mlflow.end_run()
    except:
        None

    with mlflow.start_run():
        try:
            model = keras.models.load_model(MODEL_PATH)
        except:
            model = get_model(X.shape[1])
        
        history = model.fit(
            X, y, epochs=n_epochs, batch_size=batch_size,
            validation_split=.2, verbose=1
        )

        mlflow.log_param('datetime', datetime.now())
        for key, value in history.history.items():
            mlflow.log_metric(key, value[-1])
        mlflow.keras.log_model(model, 'model')

        return history