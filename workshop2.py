from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.kodlama.io/")

driver.maximize_window()
sleep(4)
course = driver.find_elements(By.CLASS_NAME, ("course-listing-extra-info")) 
number_of_course = len(course)

sleep(4)
if number_of_course == 6:
    print("Kodlama.io da ki toplam kurs sayısı:" + str(course))
else:
    print("Hatalı sonuç")
driver.save_screenshot(str(date.today()) + '(1).png')
sleep(4)

search = driver.find_element(By.XPATH,'//[@name="query"]')
search.send_keys("Senior")
sleep(4)
title = driver.find_element(By.XPATH,'//[@title="Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)"]')
titleTest = title.text
print(title)
sleep(4)
if titleTest == "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)":
    print("Sonuç başarılı ")
else:
    print("Sonuç başarısız")
driver.save_screenshot(str(date.today()) + '(2).png')

driver.close()