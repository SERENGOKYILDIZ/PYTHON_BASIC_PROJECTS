import requests
import time
import smtplib
import lxml
from bs4 import BeautifulSoup


my_email = "erengokyildiz31@gmail.com"
password = "drokuoeariatymbf"
victim = "gokyildizsemieren@gmail.com"

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9,tr;q=0.8"
}
hedef_fiyat = 70
price = 0

while True:
    time.sleep(0.5)
    response = requests.get(url=URL, headers=header)
    response.raise_for_status()
    html_text = response.text

    # print(html_text)

    soup = BeautifulSoup(html_text, "lxml")
    try:
        price1 = soup.find(name="span", class_="a-price-whole").getText()
        price2 = soup.find(name="span", class_="a-price-fraction").getText()
        price = price1 + price2
        break
    except AttributeError:
        continue


if float(price) < hedef_fiyat:
    msg = f"Bizim istedigimiz fiyat: ${hedef_fiyat}'di, Anlik fiyat: ${price} oldu al bence"
    print(msg)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=victim,
            msg=f"Subject:Amazon Fiyat Alarm!!\n\n{msg}".encode("utf-8")
        )