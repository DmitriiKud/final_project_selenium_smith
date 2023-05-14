import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    """Method is getting WEB element"""

    def is_element_clickable(self, webelement):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(webelement))

    def get_element(self, by, locator):
        return self.driver.find_element(by, locator)

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot("D:\\AutotestProjects\\FinalProject\\screenshot\\" + name_screenshot)
        print("screenshot: " + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Assert url - PASSED")

    """Method assert page text"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Assert word - PASSED")
