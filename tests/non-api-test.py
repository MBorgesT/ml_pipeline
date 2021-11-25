import sys
sys.path.append("/home/matheus/Code/IC/ml_pipeline/coordinator")

from pipeline import pipeline

dir_path = '/home/matheus/Code/IC/ml_pipeline/tests/datasets/'
for i in range(5):
    file_path = dir_path + f'ds{i+1}.csv'
    file = open(file_path, 'rb')
    pipeline(file)