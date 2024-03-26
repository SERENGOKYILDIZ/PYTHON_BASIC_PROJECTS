from selenium import webdriver
from selenium.webdriver.common.by import By  # Secim yaparken gerekli
from selenium.webdriver.common.keys import Keys  # Klavye tuşlarını algılamak için
from selenium.common.exceptions import NoSuchElementException  # Öge yoksa hata verme
import time

email = "erenosim132@gmail.com"
password = "eren145369"
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
phone = "+905339755000"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

browser.get("https://www.youtube.com/")

sign_btn = browser.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_btn.click()

email_box = browser.find_element(By.ID, "username")
password_box = browser.find_element(By.ID, "password")
sign_in_btn = browser.find_element(By.CLASS_NAME, "btn__primary--large")

email_box.send_keys(email)
password_box.send_keys(password)
sign_in_btn.click()

time.sleep(1)
mal_btn = browser.find_element(By.ID, "ember114")
mal_btn.click()


def apply_job():
    save_btn = browser.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save_btn.click()
    time.sleep(0.5)
    svg = browser.find_element(By.CSS_SELECTOR, ".artdeco-toast-item__dismiss.artdeco-button.artdeco-button--circle.artdeco-button--muted.artdeco-button--1.artdeco-button--tertiary.ember-view")
    svg.click()
    time.sleep(0.1)
    browser.execute_script("window.scrollBy(0, 100)")

# apply_btn = browser.find_element(By.CSS_SELECTOR, ".jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
# apply_btn.click()
# time.sleep(2)
# phone_box = browser.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3689679460-8584083579224415603-phoneNumber-nationalNumber")
# phone_box.send_keys(phone)
# summary_box = browser.find_element(By.CSS_SELECTOR, ".fb-multiline-text.artdeco-text-input--input.artdeco-text-input__textarea.artdeco-text-input__textarea--align-top")
# summary_box.send_keys("Selam ben adal")
# headline_box = browser.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3689679460-3883271981038082173-text")
# headline_box.send_keys("")
# headline_box.send_keys("BASLIK")
# next_btn = browser.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
# next_btn.click()
#
# street_line_1_box = browser.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3689679460-3626002591588914937-text")
# street_line_1_box.send_keys("sokak 1")
# street_line_2_box = browser.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3689679460-3723138235110443518-text")
# street_line_2_box.send_keys("sokak 2")
# city_box = browser.find_element(By.CSS_SELECTOR, "#single-typeahead-entity-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3689679460-4710977228029186946-city-HOME-CITY")
# city_box.send_keys("İstanbul")
# posta_code_box = browser.find_element(By.CSS_SELECTOR, "#single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3689679460-7672996319443386234-text")
# posta_code_box.send_keys("")
# posta_code_box.send_keys("34098")
# next_btn = browser.find_element(By.CSS_SELECTOR, ".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
# next_btn.click()

jobs_link = browser.find_elements(By.CSS_SELECTOR, "li div div div div div a")
for job in jobs_link:
    try:
        job.click()
    except NoSuchElementException:
        print("Hata var aq")
        continue
    time.sleep(0.5)
    apply_job()