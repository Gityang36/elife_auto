from selenium.webdriver.common.by import By
import time
from cfg import *
from lib.webUIutility import web_utility
import pytest
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def login():
    web_utility.web_login(usr, pwd)
    web_utility.driver.get(DEVICE_URL)

def test_device_management_001(login):
    addBtn = web_utility.driver.find_element(By.CSS_SELECTOR,'.add-one-area .btn')
    if addBtn.text == '添加':
        addBtn.click()
    Select(web_utility.driver.find_element(By.ID,'device-type')).select_by_visible_text('存储柜')
    ele1 = web_utility.driver.find_element(By.ID,'device-model')
    ele1.clear()
    ele1.send_keys('elife-cabinlocker-g22-10-20-40')
    ele2 = web_utility.driver.find_element(By.ID, 'device-model-desc')
    ele2.clear()
    ele2.send_keys('南京e生活存储柜 10大20中40小')
    web_utility.driver.find_element(By.CSS_SELECTOR,'.add-one-submit-btn-div .btn').click()
