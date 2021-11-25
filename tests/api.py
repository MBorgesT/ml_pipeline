import requests

url = 'http://localhost:5001/pipeline'

def get_file_path(i):
    return f'datasets/ds{i}.csv'

for i in range(5):
    with open(get_file_path(i+1), 'rb') as f:
        r = requests.post(url, files={'file': f})
        print(r)