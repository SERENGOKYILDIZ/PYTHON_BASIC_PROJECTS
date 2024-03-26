#NOT: Diğer python dosyasındada bilgler bulunmaktadır, inceleyiniz.


from selenium import webdriver
from selenium.webdriver.common.by import By #Secim yaparken gerekli

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=options)

# browser.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# price = browser.find_element(By.CLASS_NAME, "a-price-whole") #CLASS türünden 'a-price-whole' olan elemanı sectik
# print(price.text)




browser.get("https://www.python.org/")

# search_box = browser.find_element(By.NAME, "q")
# print(search_box.tag_name)
# print(search_box.get_attribute("placeholder"))

# logo = browser.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# doc_link = browser.find_element(By.CSS_SELECTOR, ".documentation-widget p a")
# print(doc_link.text)

# bug_link = browser.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

#MEYDAN OKUMA
times = browser.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery ul li time")
names = browser.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery ul li a")

event_dict = {str(num): {"time": times[num].text, "name": names[num].text} for num in range(5)}

print(event_dict)













# browser.close() #Belirli sayfa kapatır
browser.quit() #tamamen kapatır