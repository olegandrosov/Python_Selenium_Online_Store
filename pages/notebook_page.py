import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Notebook_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    laptop_button = "//a[@href='noutbuki']"
    macbook_button = "//*[@id='mfilter-content-container']/div[1]/div[3]/div[2]/a[1]"

    # Getters

    def get_laptop_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.laptop_button)))

    def get_macbook_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.macbook_button)))

    # Actions

    def click_laptop_button(self):
        self.get_laptop_button().click()
        print("Переход на страницу ноутбуков")

    def click_macbook_button(self):
        self.get_macbook_button().click()
        print("Переход на страницу макбуков")

    # Methods
    """Переход на страницу ноутбуков и выбор ноутбуков марки Apple"""
    def select_macbook(self):
        with allure.step("Select macbook"):
            Logger.add_start_step(method="select_macbook")
            self.click_laptop_button()
            self.click_macbook_button()
            Logger.add_end_step(url=self.driver.current_url, method="select_macbook")
