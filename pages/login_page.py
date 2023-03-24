import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    user_email = "//input[@id='input-email']"
    password = "//input[@id='input-password']"
    login_button = "//input[@type='submit']"
    login_word = "//*[@id='content']/h2[1]"

    # Getters

    def get_user_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_word)))

    # Actions

    def input_user_email(self, user_email):
        self.get_user_email().send_keys(user_email)
        print("Ввеcти почту пользователя")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввести пароль")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажать кнопку войти")

    # Methods
    """Ввод информации пользователя и вход в учетную запись"""
    def authorization(self):
        self.input_user_email("test1@gmail.com")
        self.input_password("66677767")
        self.click_login_button()
        self.assert_word(self.get_login_word(), "Моя учетная запись")
        print("Вход в учетную запись выполнен")
