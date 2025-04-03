import requests 
import json


def fetch_bike_data():
    url = "https://api.tfl.gov.uk/BikePoint"
    response = requests.get(url)
    data = response.json()

    #save the data to a local json file or database
    with open('data/bike_data.json', 'w') as f:
        json.dump(data, f)
    return data 