import datetime
from time import strftime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(value_word + " идентичен " + result)

    """Method screenshot"""

    def get_screenshot(self):
        now_date = (datetime.datetime.utcnow() + datetime.timedelta(hours=+3)).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot_" + now_date + ".png"
        self.driver.save_screenshot(f'./screen/ {name_screenshot}')
        print("Screenshot: " + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(get_url + " идентичен " + result)

    """Method assert price"""

    def assert_price(self, price1, price2):
        assert price1 == price2
        print(price1 + " = " + price2)

    """Method assert names"""

    def assert_text(self, word, result):
        assert word == result
        print(word + " = " + result)

