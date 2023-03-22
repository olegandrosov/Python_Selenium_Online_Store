import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.macbook_page import Macbook_page
from pages.main_page import Main_page
from pages.notebook_page import Notebook_page


def test_select_product_1(set_module):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    g = Service('C:\\Users\\Oleg\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    print("Begin Test 1")

    mp = Main_page(driver)
    mp.enter_login_page()

    lp = Login_page(driver)
    lp.authorization()

    np = Notebook_page(driver)
    np.select_macbook()

    mp = Macbook_page(driver)
    mp.add_macbook()

    cp = Cart_page(driver)
    cp.cart_options()
