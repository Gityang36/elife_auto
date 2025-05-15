import pytest
from lib.webUIutility import web_utility

@pytest.fixture()
def clear_alert():
    yield
    try:
        web_utility.driver.switch_to.alert.accept()
    except Exception as e:
        print(e)