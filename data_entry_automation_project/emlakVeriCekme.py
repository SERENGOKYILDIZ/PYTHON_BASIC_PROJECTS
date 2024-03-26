from pprint import pprint

import requests
from bs4 import BeautifulSoup

EMLAK_URL = "https://bit.ly/3odWHXp"


class EmlakVerileri:
    def __init__(self):
        self.soup = 0
        self.links = []
        self.address = []
        self.price = []
        self.JSON = []

    def getLinks(self):
        response = requests.get(url="https://www.emlakjet.com/kiralik-konut/istanbul/")
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, "html.parser")
        links = self.soup.select(selector="#listing-search-wrapper div a")
        self.links = []
        for item in links:
            try:
                if item.get("href")[:6] == "/ilan/":
                    self.links.append(f"https://www.emlakjet.com{item.get('href')}")
            except TypeError:
                continue

        # for item in self.links:
        #     print(item)

    def getAddress(self):
        response = requests.get(url="https://www.emlakjet.com/kiralik-konut/istanbul/")
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, "html.parser")

        address = self.soup.select(selector="#listing-search-wrapper div a div div div span")
        self.address = [item.text for item in address if item.text[:2] == "İs"]

        # for item in self.address:
        #     print(item)

    def getPrices(self):
        response = requests.get(url="https://www.emlakjet.com/kiralik-konut/istanbul/")
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, "html.parser")

        self.price = self.soup.select(selector="#listing-search-wrapper div a div div div div p span span")

        # for item in self.prices:
        #     print(item.text)

    def setJson(self):
        self.JSON = []
        for index in range(30):
            new_dict = {"link": self.links[index], "address": self.address[index], "price": self.price[index].text}
            self.JSON.append(new_dict)
        # pprint(self.JSON)