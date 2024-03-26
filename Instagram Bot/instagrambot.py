from selenium import webdriver
from selenium.webdriver.common.by import By  # Secim yaparken gerekli
from selenium.webdriver.common.keys import Keys  # Klavye tuşlarını algılamak için
from selenium.common.exceptions import NoSuchElementException  # Öge yoksa hata verme
from selenium.common.exceptions import ElementClickInterceptedException  # Tıklanma hatası
import time

INSTAGRAM_USERNAME = "engibicov"
INSTAGRAM_EMAIL = "jaybicovseren132@gmail.com"
INSTAGRAM_PASSWORD = "osman=eren?1453:"

URL = "https://www.instagram.com/accounts/login/"


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)

    def login(self):
        self.browser.get(URL)
        self.browser.maximize_window()
        time.sleep(1)

        email_box = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        email_box.send_keys(INSTAGRAM_EMAIL)
        password_box = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        password_box.send_keys(INSTAGRAM_PASSWORD)
        password_box.send_keys(Keys.ENTER)
        time.sleep(3)

    def find_followers(self, user: str):
        self.browser.get(f"https://www.instagram.com/{user}/")
        time.sleep(3)

        followers_btn = self.browser.find_element(By.CSS_SELECTOR, "section ul li a")
        followers_btn.click()
        time.sleep(2)

    def follow(self):
        yeni_takipci = 0
        toplam_adam_sayisi = 0
        # Number of followers
        number_of_followers = self.browser.find_element(By.CSS_SELECTOR, "section ul li a span span")
        number = int(number_of_followers.text.split(".")[0]) * 1000
        print(number)
        for i in range(100):
            bar = self.browser.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bar)
            time.sleep(0.2)

        all_buttons = self.browser.find_elements(By.CSS_SELECTOR, "div div div div div div div div div div div div div div div div div div div div button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(0.2)
            except ElementClickInterceptedException:
                cancel_button = self.browser.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]")
                cancel_button.click()
            else:
                yeni_takipci += 1
            finally:
                toplam_adam_sayisi += 1
            print(f"Yeni eklenen arkadaslar = {yeni_takipci} oldu!, Toplam = {toplam_adam_sayisi}")
