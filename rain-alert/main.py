import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "ada48f57de10391acd1f192ffe220610"

phone_num = "+12188455320"
hedef = "+905338175581"
account_sid = "ACfbc12e0266d302396b93224e391e7b29"
auth_token = "5ee99279d109c2f1c40b2acd32d527f9"

parameters = {
    "lat": 43.110718,
    "lon": 12.390828,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


def check_weather(hour: dict):
    return hour["weather"][0]["id"]


response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather_data = weather_data["hourly"]

is_Rain = False
for i in range(12):
    if check_weather(hourly_weather_data[i]) < 700:
        is_Rain = True

if is_Rain:
    print("Yagmur var")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Yagmur yagacak lan",
        from_=phone_num,
        to=hedef
    )
    print(message.status)