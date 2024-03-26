from selenium import webdriver
from selenium.webdriver.common.by import By  # Secim yaparken gerekli
from selenium.webdriver.common.keys import Keys  # Klavye tuşlarını algılamak için
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

aralik = 5 * 60  # 5 dakika

browser.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(1)
lan_btn = browser.find_element(By.CSS_SELECTOR, ".langSelectButton.title")
lan_btn.click()

time.sleep(1)
cookie_btn = browser.find_element(By.ID, "bigCookie")
while True:
    cookie_count = browser.find_element(By.ID, "cookies")
    timeout = time.time() + aralik
    while time.time() <= timeout:
        cookie_btn.click()

    products = browser.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    prices = [int(products[x].text.split()[1]) for x in range(len(products))]
    index = prices.index(max(prices))

    # products[index].click()
    browser.execute_script("arguments[0].click();", products[index]) #Tıklama sorununu çözdü

    durum = browser.find_element(By.ID, "cookiesPerSecond").text
    print(f"Cookies/Second: {float(durum.split()[2])}")
