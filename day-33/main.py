import requests

# response = requests.get(url="http://api.open-notify.org/is-now.json") #HATA YAPTIK
# response.raise_for_status()

# response = requests.get(url="http://api.open-notify.org/iss-now.json") #GET ile veri istedik cevabı değişkene atadık
# print(response) # <Response [200]> yazar; Bu 200 cevabı veriyi başarılı bir şekilde aldım demek
# print(response.status_code) #Cevap kodu = 200. Anlamı; Başarılı, 404 olsaydı bulunamadı olurdu
# data = response.json()
# print(data)

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T"))
print(sunset.split("T"))