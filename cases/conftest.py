import pytest
from selenium.webdriver.common.by import By

from lib.webUIutility import web_utility
from cfg import *

@pytest.fixture()
def clear_alert():
    yield
    try:
        web_utility.driver.switch_to.alert.accept()
    except Exception as e:
        print(e)

@pytest.fixture(scope='module')
def login_ready():
    web_utility.web_login(usr,pwd)
    chk_login = web_utility.driver.find_elements(By.TAG_NAME,'nav')
    assert chk_login != []
@pytest.fixture(scope='function')
def del_dev():
    yield
    print('删除第一个设备')
    web_utility.delete_last_added_dev()