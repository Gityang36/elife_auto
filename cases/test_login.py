from selenium.webdriver.common.by import By
import time
from cfg import *
from lib.webUIutility import web_utility
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_smp_login_001():
    web_utility.web_login(usr,pwd)
    # 返回所有匹配定位策略的元素（即使只有一个或零个）。
    # 如果未找到元素，返回空列表（不会抛出异常）
    chk_login = web_utility.driver.find_elements(By.TAG_NAME,'nav')
    assert chk_login != []

@pytest.mark.parametrize('username,password,pop_alert',[
    (None,pwd,'请输入用户名'),
    ('byhy',None,'请输入密码'),
    ('any',pwd,'登录失败： 用户名不存在')
])
def test_smp_login_002(username,password,pop_alert,clear_alert):
    web_utility.web_login(username, password)
    WebDriverWait(web_utility.driver, 2).until(EC.alert_is_present())
    alert = web_utility.driver.switch_to.alert
    assert alert.text == pop_alert

