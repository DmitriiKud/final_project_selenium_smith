from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage

import time

"""Данный тест авторизуется в магазине exist.ru и покупает мне масло KIXX с применением фильтров, переключением на iframe
 и оформлением заказа. В конце также делает скриншот"""

def test_buy_product_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # убирает служебные сообщения в консоли
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

    mp = MainPage(driver)
    mp.authorization()
    mp.choose_product()

    time.sleep(3)