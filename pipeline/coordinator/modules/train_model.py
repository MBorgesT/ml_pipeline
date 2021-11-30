from . import ml
from sklearn.preprocessing import StandardScaler

def run(df):
    X = df.values[:, :-1]
    X = StandardScaler().fit_transform(X)

    y = df.values[:, -1].flatten()

    ml.train_model(X, y)