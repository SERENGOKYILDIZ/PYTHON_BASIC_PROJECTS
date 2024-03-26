from selenium import webdriver
from selenium.webdriver.common.by import By  # Secim yaparken gerekli
from selenium.webdriver.common.keys import Keys  # Klavye tuşlarını algılamak için
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)


# browser.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_count = browser.find_element(By.CSS_SELECTOR, "#articlecount a")
# # print(article_count.text)
# # article_count.click() #Belirtilen linkin üzerine tıklar.
#
# # content_portals = browser.find_element(By.LINK_TEXT, "Content portals")
# # content_portals.click()
#
# search_box = browser.find_element(By.CSS_SELECTOR, ".cdx-text-input__input")
# search_box.send_keys("Abdülhamid")
#
# #1.Yol #Kendim olarak 2.Seçeneği tanımladım
# # time.sleep(0.2)
# # choice_item = browser.find_element(By.XPATH, "//*[@id='cdx-menu-item-2']/a")
# # choice_item.click()
#
# #2.Yol #Direk isim ile ara
# search_box.send_keys(Keys.ENTER)
#
#
#
#
#
#
#
# # browser.quit()


# Meydan Okuma
browser.get("http://secure-retreat-92358.herokuapp.com/")

first_name = browser.find_element(By.NAME, "fName")
second_name = browser.find_element(By.NAME, "lName")
email = browser.find_element(By.NAME, "email")
sign_up_btn = browser.find_element(By.CLASS_NAME, "btn")

first_name.send_keys("Semi Eren")
second_name.send_keys("Gökyıldız")
email.send_keys("erenosim132@gmail.com")
sign_up_btn.send_keys(Keys.ENTER)
