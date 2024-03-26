from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data_manager.get_cities()
print("Sehir verileri çekildi.")
for city in data_manager.cities:
    flight_search.get_IATA(city)
print("IATA verileri çekildi.")
data_manager.put_IATA()
print("IATA verileri tabloya aktarıldı.")

for city in data_manager.cities:
    flight = flight_search.get_to_LONDON(city)
    if flight.price < city["lowestPrice"]:
        notification_manager.send_email(f"{city['price']}")