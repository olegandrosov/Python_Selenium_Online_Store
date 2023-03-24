import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_magazine = "//div[@class='category-warehouses-select']"
    comment = "//textarea[@id='input-comment']"
    delete_button = "//*[@class='btn btn-danger']"
    empty_cart = "//*[@id='content']/p"
    logo_company = "//a[@href='https://xtel-lg.com/']"

    # Getters

    def get_select_magazine(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_magazine)))

    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))

    def get_empty_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart)))

    def get_logo_company(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logo_company)))

    # Actions

    def click_select_magazine(self):
        self.get_select_magazine().click()
        print("Нажатие на выбор магазина")

    def input_comment(self, text):
        self.get_comment().send_keys(text)
        print("Комментарий успешно вставлен")

    def click_delete_button(self):
        self.get_delete_button().click()
        print("Товар удален из корзины")

    def click_get_logo_company(self):
        self.get_logo_company().click()
        print("Вернулись на главную страницу магазина")

    # Methods
    """Проверка доступных магазинов, добавление комментария к заказу, очистка корзины, возвращение на главную 
    страницу"""
    def cart_options(self):
        self.click_select_magazine()
        self.input_comment("Заберу заказ после 15:00")
        self.click_delete_button()
        self.assert_word(self.get_empty_cart_word(), "Ваша корзина пуста!")
        self.click_get_logo_company()
        self.get_screenshot()
