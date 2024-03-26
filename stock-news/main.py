STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import requests
import datetime as dt
import smtplib
import time

now = dt.datetime.now()
yesterday = now - dt.timedelta(days = 1)

STOCK_API_KEY = "Z6ZGLACA7V668FY9"
STOCK_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
STOCK_response = requests.get(url="https://www.alphavantage.co/query", params=STOCK_parameters)
STOCK_response.raise_for_status()
STOCK_data = STOCK_response.json()

ONCEKI_GUN_Price = float(STOCK_data["Time Series (Daily)"][list(STOCK_data["Time Series (Daily)"].keys())[1]]["4. close"])
SIMDIKI_GUN_Price = float(STOCK_data["Time Series (Daily)"][list(STOCK_data["Time Series (Daily)"].keys())[0]]["4. close"])

Fark = ONCEKI_GUN_Price - SIMDIKI_GUN_Price
Yuzde_Fark = (Fark*100)/ONCEKI_GUN_Price

print(ONCEKI_GUN_Price)
print(SIMDIKI_GUN_Price)
print(Fark)
print(f"TSLA = %{'{:.2f}'.format(Yuzde_Fark)} degisim")

print(yesterday.date())

News_KEY = "e85be02c1ad942c08b88a2f29076ae20"
News_parameters = {
    "q": "Tesla",
    "from": "2023-08-02",
    "sortBy": "popularity",
    "apikey": News_KEY
}

time.sleep(5)

News_response = requests.get(url="https://newsapi.org/v2/everything", params=News_parameters)
News_response.raise_for_status()
News_data = News_response.json()

Daily_News = News_data["articles"][0]["description"]
print(Daily_News)

my_email = "erengokyildiz31@gmail.com"
password = "drokuoeariatymbf"
victim = "gokyildizsemieren@gmail.com"

time.sleep(5)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=victim, msg=f"Subject:{'{:.2f}'.format(Yuzde_Fark)} Degisim\n\n Haberlere bak")

    print(f"Subject:{'{:.2f}'.format(Yuzde_Fark)} Degisim\n\n{Daily_News}")
    print("... GİTTİ")
