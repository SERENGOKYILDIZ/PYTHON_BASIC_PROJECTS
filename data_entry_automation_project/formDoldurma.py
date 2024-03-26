from selenium import webdriver
from selenium.webdriver.common.by import By  # Secim yaparken gerekli
from selenium.webdriver.common.keys import Keys  # Klavye tuşlarını algılamak için
from selenium.common.exceptions import NoSuchElementException  # Öge yoksa hata verme
from selenium.common.exceptions import ElementClickInterceptedException  # Tıklanma hatası
import time

FORM_URL = "https://forms.gle/aKAsGinEVTcHmm1r8"


class FormDolduran:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        
        self.browser.maximize_window()
        self.browser.get(url=FORM_URL)
        time.sleep(3)

    def setForm(self, JSON: list):
        for item in JSON:
            print(f'{item["address"]} / {item["price"]} / {item["link"]}')
            adres_box = self.browser.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            adres_box.send_keys(item["address"])
            fiyat_box = self.browser.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            fiyat_box.send_keys(item["price"])
            link_box = self.browser.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link_box.send_keys(item["link"])
            send_btn = self.browser.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
            send_btn.click()
            time.sleep(0.2)
            self.browser.get(url=FORM_URL)
            time.sleep(0.2)
