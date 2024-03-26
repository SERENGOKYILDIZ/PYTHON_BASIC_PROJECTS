from selenium import webdriver
from selenium.webdriver.common.by import By  # Secim yaparken gerekli
from selenium.webdriver.common.keys import Keys  # Klavye tuşlarını algılamak için
from selenium.common.exceptions import NoSuchElementException  # Öge yoksa hata verme
import time

X_EMAIL = "erengokyildiz31@gmail.com"
X_USERNAME = "ErenGkyldz12010"
X_PASSWORD = "eren145369"
DOWN = 100
UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)

        self.DOWN = 0
        self.UP = 0

    def get_internet_speed(self):
        self.browser.get(url="https://www.speedtest.net")
        time.sleep(0.3)
        pop_btn = self.browser.find_element(By.ID, "onetrust-close-btn-container")
        pop_btn.click()

        start_btn = self.browser.find_element(By.CSS_SELECTOR, "a .start-text")
        start_btn.click()

        time.sleep(60)

        down_text = self.browser.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        up_text = self.browser.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")

        self.DOWN = float(down_text.text)
        self.UP = float(up_text.text)

        print(f"DOWN = {self.DOWN}, UP = {self.UP}")
        pass

    def tweet_at_provider(self):
        self.browser.get("https://twitter.com/home?lang=tr")
        time.sleep(1)

        sign_btn = self.browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span")
        sign_btn.click()
        time.sleep(1)

        email_box = self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_box.send_keys(X_EMAIL)
        email_box.send_keys(Keys.ENTER)
        time.sleep(1)

        username_box = self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        username_box.send_keys(X_USERNAME)
        username_box.send_keys(Keys.ENTER)
        time.sleep(1)

        password_box = self.browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password_box.send_keys(X_PASSWORD)
        password_box.send_keys(Keys.ENTER)
        time.sleep(5)

        MSG = f"Vaat edilen internet 100mps olması gerekirken test sonucu = {self.DOWN} mps indirme, {self.UP} mps yükleme"
        post_box = self.browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
        post_box.send_keys(MSG)

        post_btn = self.browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]")
        post_btn.send_keys(Keys.ENTER)
        pass
