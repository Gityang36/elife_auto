import pytest
from lib.webUIutility import web_utility

@pytest.fixture(scope='module',autouse=True)
def close_browser():
    web_utility.driver.quit()