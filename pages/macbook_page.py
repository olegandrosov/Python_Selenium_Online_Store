import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Macbook_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    mac_name_main_value = ''
    mac_name_cart_value = ''
    mac_price_1_value = ''
    mac_price_2_value = ''

    # Locators

    laptop_button = "//a[@href='noutbuki']"
    macbook_button = "//*[@id='mfilter-content-container']/div[1]/div[3]/div[2]/a[1]"
    right_slider = "//*[@id='scale-price']/div[1]/div[2]/div"
    diagonal_13_checkbox = "//*[@id='v-107854292993974']/small"
    confirm_filter_button = "//*[@id='ocfilter']/div[4]/div[2]/button"
    select_macbook_air = "//*[@id='mfilter-content-container']/div[5]/div/div/div/div[2]/div[1]/a"
    add_to_cart_macbook = "//input[@id='button-cart']"
    cart_button = "//div[@class='total-price-basket']"
    cart_open = "//a[@class='button btn-view-cart inverse']"
    mac_word = "//*[@id='quickview_product']/div[2]/div/h1"
    mac_cart_word = "//*[@id='content']/form/div/table/tbody/tr[1]/td[2]/a"
    mac_price = "//span[@id='price-old']"
    mac_cart_price = "//*[@id='content']/form/div/table/tbody/tr[3]/td[3]"

    # Getters

    def get_right_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.right_slider)))

    def get_button_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_filter_button)))

    def get_diagonal_13_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.diagonal_13_checkbox)))

    def get_select_macbook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_macbook_air)))

    def get_add_to_cart_macbook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_macbook)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_cart_open(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_open)))

    def get_mac_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_word)))

    def get_mac_cart_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_cart_word)))

    # Actions

    def move_slider(self, slider_getter, value_1, value_2):
        action = ActionChains(self.driver)
        slider = action.click_and_hold(slider_getter).move_by_offset(value_1, value_2).release().perform()
        print("Перемещение слайдера произведено")
        return slider

    def click_confirm_filter_button(self):
        self.get_button_confirm().click()
        print("Фильтр подтвержден")

    def click_diagonal_13_checkbox(self):
        self.get_diagonal_13_checkbox().click()
        print("Показаны товары только с 13 диагональю экрана")

    def click_select_macbook_air(self):
        self.get_select_macbook().click()
        print("Переход на карточку товара успешно выполнен")

    def click_add_to_cart_macbook(self):
        self.get_add_to_cart_macbook().click()
        print("Товар добавлен в корзину")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Всплывающее окно корзины открыто")

    def click_cart_open(self):
        self.get_cart_open().click()
        print("Осуществлен переход на страницу корзины")

    def get_mac_price_main(self):
        global mac_price_1_value
        mac_price_1 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_price)))
        mac_price_1_value = mac_price_1.text
        print(mac_price_1_value)
        return mac_price_1_value

    def get_mac_price_cart(self):
        global mac_price_2_value
        mac_price_2 = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_cart_price)))
        mac_price_2_value = mac_price_2.text
        print(mac_price_2_value)
        return mac_price_2_value

    def get_mac_name_main(self):
        global mac_name_main_value
        mac_name_main = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_word)))
        mac_name_main_value = mac_name_main.text
        print(mac_name_main_value)
        return mac_name_main_value

    def get_mac_name_cart(self):
        global mac_name_cart_value
        mac_name_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mac_cart_word)))
        mac_name_cart_value = mac_name_cart.text
        print(mac_name_cart_value)
        return mac_name_cart_value

    # Methods
    """Проверка работы фильтров, добавление товара в корзину и переход в нее, сравнение цены и наименования товара между 
    страницей карточки товара и корзиной"""
    def add_macbook(self):
        self.move_slider(self.get_right_slider(), -10, 0)
        self.click_confirm_filter_button()
        self.click_diagonal_13_checkbox()
        self.click_confirm_filter_button()
        self.click_select_macbook_air()
        self.get_mac_name_main()
        self.get_mac_price_main()
        # self.assert_word(self.get_mac_word(), "Ноутбук Apple MacBook Air 13'' FHD M1 7-core/8Gb/256Gb")
        self.click_add_to_cart_macbook()
        self.click_cart_button()
        self.click_cart_open()
        self.get_mac_name_cart()
        self.get_mac_price_cart()
        self.assert_text(mac_name_main_value, mac_name_cart_value)
        self.assert_price(mac_price_1_value, mac_price_2_value)
        self.assert_url("https://xtel-lg.com/index.php?route=checkout/buy")
        # self.assert_word(self.get_mac_cart_word(), "Ноутбук Apple MacBook Air 13'' FHD M1 7-core/8Gb/256Gb")
        # self.driver.close()
