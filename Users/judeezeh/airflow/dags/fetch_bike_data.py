# fetch_bike_data.py
import requests
import pandas as pd

def fetch_data():  
    url = "https://api.citybik.es/v2/networks"  
    response = requests.get(url)
    data = response.json()

    networks = data['networks']
    df = pd.json_normalize(networks)

    df.to_csv('/Users/judeezeh/Desktop/Zoomcamp-project/data/bike_data.csv', index=False)



