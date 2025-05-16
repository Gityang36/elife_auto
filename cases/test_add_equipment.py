from selenium.webdriver.common.by import By
import time

from lib.webUIutility import web_utility
import pytest


def test_add_equipment_locker(login_ready,del_dev):
    web_utility.driver.find_element(By.XPATH,'/html/body/ul/li[2]/a').click()
    web_utility.driver.find_element(By.CLASS_NAME,'btn').click()
    web_utility.driver.find_element(By.XPATH,'//*[@id="device-type"]/option[1]').click()
    web_utility.driver.find_element(By.ID,'device-model').send_keys('cabinlocker-g22-10-20')
    web_utility.driver.find_element(By.ID,'device-model-desc').send_keys('北京e生活存储柜-10')
    web_utility.driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[4]/span').click()
    dev = web_utility.get_device_list()
    print(dev)
    if dev == ['存储柜','cabinlocker-g22-10-20', '北京e生活存储柜-10']:
        print('check pass')

