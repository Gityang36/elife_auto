from gevent.subprocess import value
from selenium.webdriver.common.by import By
import time
from cfg import *
from lib.webUIutility import web_utility
import pytest




web_utility.web_login(usr,pwd)
chk_login = web_utility.driver.find_elements(By.TAG_NAME,'nav')
assert chk_login != []


web_utility.driver.find_element(By.XPATH,'/html/body/ul/li[2]/a').click()
# val_list = []
# values = web_utility.driver.find_elements(By.CLASS_NAME,'field-value')
# i = 0
# for item in values:
#     val_list.append(item.text)
#     i += 1
#     if i % 3 == 0:
#         break
#
# print(val_list)
# values = web_utility.driver.find_elements(By.CSS_SELECTOR,'.field-value')
# print(values)
dev = web_utility.get_device_list()
print(dev)
if dev == ['存储柜', 'cabinlocker-g22-10-20', '北京e生活存储柜-10']:
    print('check pass')
else:
    print('fail')
