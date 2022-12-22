from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pathlib import Path
from constants import *
from time import sleep


class Test_Saucedemo:
    
    def setup_method(self): 

        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1050, 662)
        self.driver.get(BASE_DOMAIN_URL)   
        # self.driver.get("https://www.saucedemo.com/")
    
    def teardown_method(self, method):
     self.driver.quit()



              #Doğru bilgilerden standard_user kullanıcı adıyla giriş yapılmanın doğru olup olmadığı kontrol edilmelidir.#
       
    def test_login(self):
    
          WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"*[data-test=\"username\"]" )))
          username= self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]" )
          username.send_keys(USERNAME)

          WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"*[data-test=\"password\"]")))
          password= self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]")
          password.send_keys(PASSWORD)

          WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
          loginBtn= self.driver.find_element(By.ID, LOGİN_BTN)
          loginBtn.click()

          WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USER_MENU )))
          menu= self.driver.find_element(By.ID, USER_MENU)
          menuText= menu.text
          assert menuText == MENU_TEXT





                         #Yanlış bilgiler girildiğinde uyarı çıkıp çıkmadığı test edilmelidir.#
    def test_login_unsuccess(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        username= self.driver.find_element(By.ID, USERNAME_ID )
        username.send_keys(USERNAME)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        password= self.driver.find_element(By.ID, PASSWORD_ID )
        password.send_keys(WRONG_PASSWORD)

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, USERNAME_ID )))
        loginBtn= self.driver.find_element(By.ID, LOGİN_BTN)
        loginBtn.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, ERROR)))
        error= self.driver.find_elements(By.XPATH, ERROR)
        errorLen = len(error)

        assert errorLen > 0 




        
                    #Yanlış bilgiler girildiğinde çıkan uyarı mesajının doğruluğu kontrol edilmelidir.# 
                     
    def test_login_error_message(self):
        self.test_login_unsuccess()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"*[data-test=\"error\"]")))
        error= self.driver.find_element(By.XPATH, ERROR)
        errorText = error.text

        assert errorText == ERROR_LOGİN
         

                             #Ana sayfada 6 adet ürün listelendiği kontrol edilmelidir.#


    def test_product_list(self):
        self.driver.get(BASE_DOMAIN_URL)
        username = self.driver.find_element(By.XPATH, USERNAME_ID)
        username.send_keys("standard_user")
        sleep(4)

        password = self.driver.find_element(By.XPATH, USERNAME_ID)
        password.send_keys("secret_sauce")
        sleep(4)

        login = self.driver.find_element(By.XPATH, USERNAME_ID)
        login.click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='header_container']/div[2]/span")))

        product = self.driver.find_elements(By.CLASS_NAME, ("inventory_item"))
        count = len(product)

        assert count == 6

        
   
                        #Sepete Ekle butonuna tıklandığında butonun texti REMOVE olmalıdır.#
    def test_basket(self):
        self.test_login_unsuccess()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, ADD_TO_CARD)))
        addToCard= self.driver.find_element(By.ID, ADD_TO_CARD)
        addToCard.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.NAME, PRODUCT_REMOVE_NAME)))
        productRemove = self.driver.find_element(By.NAME, PRODUCT_REMOVE_NAME)
        removeText = productRemove.text

        assert removeText == PRODUCT_REMOVE_TEXT
        
    
                   #Sepete 1 adet ürün eklendiğinde sağ üstteki sepet üzerinden "1" sayısı çıkmalıdır.#
    def test_basket_item(self):
        self.test_login_unsuccess()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID, ADD_TO_CARD)))
        addToCard = self.driver.find_element(By.ID, ADD_TO_CARD)
        addToCard.click()

        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, BASKET)))
        basketItem = self.driver.find_element(By.CLASS_NAME, BASKET)
        itemText = basketItem.text

        assert itemText == BASKET_COUNT