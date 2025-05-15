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

web_utility = WEB_UTILITY()
