import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "erenosim"
TOKEN = "a5sadfsa6df4sadf65asd6fasd45f"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_parameters = {
    "id": GRAPH_ID,
    "name": "Takip Program",
    "unit": "hour",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
date = datetime(year=2023, month=7, day=31)
print(today.strftime("%Y%m%d"))
print(date.strftime("%Y%m%d"))

post_pixel_parameters = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "5"
}
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
# print(response.text)

DATETIME = today.strftime("%Y%m%d")
PUT_post_pixel_parameters = {
    "quantity": "10"
}
PUT_post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATETIME}"

response = requests.put(url=PUT_post_pixel_endpoint, json=PUT_post_pixel_parameters, headers=headers)
print(response.text)