import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_API_KEY = "mrgX2cvTzm4N8pSMtYw_S0d8docI4mDR"


class FlightSearch:
    def get_IATA(self, city: dict):
        get_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        # print(city)
        headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application/json"
        }
        body = {
            "term": city["city"],
            "location_types": "city"
        }
        response = requests.get(url=get_endpoint, params=body, headers=headers)
        response.raise_for_status()
        datas = response.json()
        IATA = datas["locations"][0]["code"]
        city["iataCode"] = IATA

    def get_to_LONDON(self, city: dict):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"

        now = datetime.now()
        yesterday = (now + timedelta(days=1)).strftime('%d/%m/%Y')
        six_month = (now + timedelta(days=30 * 6)).strftime('%d/%m/%Y')

        headers = {
            "apikey": TEQUILA_API_KEY,
            "accept": "application/json"
        }
        body = {
            "fly_from": "LON",
            "fly_to": city["iataCode"],
            "date_from": yesterday,
            "date_to": six_month,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=search_endpoint, params=body, headers=headers)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city['iataCode']}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
