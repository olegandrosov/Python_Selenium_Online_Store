from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url_main = "https://xtel-lg.com/"

    # Locators

    login_page_button = "//a[@href='/login/']"

    # Getters

    def get_login_page_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_page_button)))

    # Actions

    def click_login_page_button(self):
        self.get_login_page_button().click()

    # Methods
    """Открытие главной страницы магазина и переход на страницу авторизации"""
    def enter_login_page(self):
        with allure.step("Enter login page"):
            Logger.add_start_step(method="enter_login_page")
            self.driver.get(self.url_main)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_login_page_button()
            self.assert_url("https://xtel-lg.com/login/")
            Logger.add_end_step(url=self.driver.current_url, method="enter_login_page")
