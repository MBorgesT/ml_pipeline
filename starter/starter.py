import requests

url = 'http://localhost:5001/pipeline'
file = 'datasets/ds1.csv'

with open(file, 'rb') as f:
    r = requests.post(url, files={'file': f})
    print(r)