from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from cfg import *

class WEB_UTILITY():
    def __init__(self):
        service = Service(executable_path=r'D:\Programs\ChromeDriverForPython\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)


    def web_login(self,username,password):
        self.driver.get(SMP_URL_LOGIN)
        if username is not None:
            self.driver.find_element(By.ID, 'username').send_keys(username)
        if password is not None:
            self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'loginBtn').click()

    def get_device_list(self):
        time.sleep(1)
        val_list = []
        values = self.driver.find_elements(By.CLASS_NAME, 'field-value')
        i = 0
        for item in values:
            val_list.append(item.text)
            i += 1
            if i % 3 == 0:
                break
        return val_list
    def delete_last_added_dev(self):
        time.sleep(1)
        del_btn = self.driver.find_element(By.CSS_SELECTOR,'.result-list-item-btn-bar>span.btn-no-border')
        if not del_btn:
            return False
        del_btn.click()
        self.driver.switch_to.alert.accept()



web_utility = WEB_UTILITY()
