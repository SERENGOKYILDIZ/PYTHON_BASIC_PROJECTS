import os
import requests
import time
from pprint import pprint

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/da2fc92257b98d29887d5a8ca24e55f2/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.cities = []
        self.api_key = f"Bearer {os.environ['TOKEN']}"
        self.headers = {
            "Authorization": self.api_key
        }

    def get_cities(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        datas = response.json()
        self.cities = datas["prices"]
        # pprint(self.cities, width=1)

    def put_IATA(self):
        for city in self.cities:
            time.sleep(0.2)
            put_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            # print(city)
            put_body = {
                "price":
                    {
                        "city": city["city"],
                        "iataCode": city["iataCode"],
                        "lowestPrice": city["lowestPrice"],
                        "id": city["id"]
                    }
            }
            put_response = requests.put(url=put_endpoint, headers=self.headers, json=put_body)
            put_response.raise_for_status()
