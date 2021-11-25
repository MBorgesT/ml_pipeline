import pandas as pd
import sqlalchemy

df = pd.read_csv('FRA3-FRA6_cleaned_feature_engineered.csv')
engine = sqlalchemy.create_engine('postgresql://root:root@localhost:5002/postgres')
df.to_sql('superstore', engine)