from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from lib.webUIutility import web_utility
import pytest

def test_add_equipment_locker(login_ready,del_dev):
    web_utility.driver.find_element(By.XPATH,'/html/body/ul/li[2]/a').click()
    add_btn = web_utility.driver.find_element(By.CLASS_NAME, 'btn')
    with open('devices_to_add.txt',encoding='utf-8') as f:
        for line in f:
            line.strip()
            if line:
                devs = line.split(',')
                dev_type = devs[0]
                dev_model = devs[1]
                dev_desc = devs[2]

                if add_btn.text == '添加':
                    add_btn.click()
                select = Select(web_utility.driver.find_element(By.ID, "device-type"))
                select.select_by_visible_text(dev_type)
                ele_type = web_utility.driver.find_element(By.ID,'device-model')
                ele_type.clear()
                ele_type.send_keys(dev_model)
                ele_desc = web_utility.driver.find_element(By.ID,'device-model-desc')
                ele_desc.clear()
                ele_desc.send_keys(dev_desc)
                web_utility.driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[4]/span').click()
    # dev = web_utility.get_device_list()
    # print(dev)
    # if dev == ['存储柜','cabinlocker-g22-10-20', '北京e生活存储柜-10']:
    #     print('check pass')

