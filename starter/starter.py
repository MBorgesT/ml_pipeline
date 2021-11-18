import requests

url = 'http://localhost:5000/'
file = 'FRA3-FRA6_cleaned_feature_engineered.csv'

with open(file, 'rb') as f:
    r = requests.post(url, files={'file': f})
    print(r)