import pandas as pd
import os
import shutil

if os.path.exists('datasets/') and os.path.isdir('datasets/'):
    shutil.rmtree('datasets/')

os.mkdir('datasets/')

original_df = pd.read_csv('FRA3-FRA6_cleaned_feature_engineered.csv')
n_rows = original_df.shape[0]
cols = list(original_df)
print(f'n_rows: {n_rows}')

n_datasets = 5
dataset_size = int(n_rows / n_datasets)
aux = 0
for i in range(n_datasets):
    start_index = i * dataset_size
    if i != n_datasets - 1:
        df = pd.DataFrame(original_df[start_index:start_index + dataset_size], columns=cols)
    else:
        df = pd.DataFrame(original_df[start_index:], columns=cols)
    aux += df.shape[0]
    df.to_csv(f'datasets/ds{i+1}.csv', encoding='utf-8', index=False)

    
print(f'aux: {aux}')