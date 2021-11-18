from pipeline import pipeline

dir_path = '/home/matheus/IC/pipeline/starter/datasets/'
for i in range(5):
    file_path = dir_path + f'ds{i+1}.csv'
    file = open(file_path, 'rb')
    pipeline(file)