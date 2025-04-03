import requests
import json 

def ingest_bike_data():
    url = "https://api.tfl.gov.uk/BikePoint"
    response = requests.get(url)
    bike_data = response.json()


    # save data to a file or GCS 
    with open("bike_data.json", "w") as f:
        json.dump(bike_data, f)

    return "bike_data.json"