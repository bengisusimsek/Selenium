from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()

#Başarısız Senaryo: 

driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(3)
input = driver.find_element(By.NAME, "email") 
input.send_keys("Bengisu")
sleep(3)

loginBtn = driver.find_element(By.ID,"email")
loginBtnText = loginBtn.text

#windows 
if loginBtnText == "Giriş Yap":
    print("Test başarılı 😎")
else:
    print("Test Başarısız ❌")


#Başarısız Senaryo: 


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(5)

input = driver.find_element(By.NAME, "email") 
input.send_keys("Bengisu")
sleep(5)
input = driver.find_element(By.NAME,"pass")
input.send_keys("Şimşek")
sleep(3)

loginBtn.click()

loginBtn = driver.find_element(By.ID,"email")
loginBtnText = loginBtn.text

#windows
if loginBtnText == "Giriş Yap":
    print("Test başarılı 😎")
else:
    print("Test Başarısız ❌")


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(3)

email = driver.find_element(By.NAME, "email")
email.click()
email.send_keys("bengisu@gmail.com")
sleep(3)

password = driver.find_element(By.NAME, "pass")
password.click()
password.send_keys("sifre")
sleep(3)

emailText = email.get_attribute('value')
passwordText= password.get_attribute('value')

loginBtn = driver.find_element(By.NAME, "login")
loginBtn.click()
sleep(3)


if(emailText == "bengisu@gmail.com" and passwordText == "sifre"):
        print("Test başarılı 😎")
else:
        print("Test başarısız❌")