import time
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    url = "https://exist.ru/"

    def __init__(self, driver):
        super().__init__(driver) # указывает на то, что это потомок класса
        self.driver = driver
        self.action = ActionChains(driver) # если нужны actionchains

    # Actions

    def click_enter_button(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.ENTER_BUTTON)).click()
        print("Click button Enter")

    def input_user_name(self, user_name):
        self.is_element_clickable(self.get_element(*MainPageLocators.USER_NAME_FIELD)).send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.is_element_clickable(self.get_element(*MainPageLocators.PASSWORD_FIELD)).send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.LOGIN_BUTTON)).click()
        print("Click button Login")

    def click_catalogue_button(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.CATALOGUE_BUTTON)).click()
        print("Click button Login")

    def click_motor_oil(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.MOTOR_OIL)).click()
        print("Click motor oil")

    def click_brand_list(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.BRAND_LIST)).click()
        print("Click brand list")

    def click_oil_brand(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.OIL_BRAND)).click()
        print("Click KIXX")

    def click_composition_list(self):
        time.sleep(2)
        self.is_element_clickable(self.get_element(*MainPageLocators.COMPOSITION_LIST)).click()
        print("Click composition list")

    def click_composition(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.COMPOSITION)).click()
        print("Click composition")

    def click_first_position(self):
        time.sleep(1)
        self.is_element_clickable(self.get_element(*MainPageLocators.FIRST_POSITION)).click()
        print("Click first oil position")

    def click_add_to_cart_button(self):
        time.sleep(1)
        # переключаемся на iframe
        self.driver.switch_to.frame(self.get_element(By.ID, "fancybox-frame"))
        self.is_element_clickable(self.get_element(*MainPageLocators.ADD_TO_CART_BUTTON)).click()
        print("Click add to cart button")

    def click_close_fancybox_button(self):
        # переключаемся обратно с iframe
        self.driver.switch_to.default_content()
        self.is_element_clickable(self.get_element(*MainPageLocators.CLOSE_FANCYBOX_BUTTON)).click()
        print("Click close fancybox")

    def click_go_to_cart_button(self):
        # скроллимся к кнопке "Корзина" и переходим в корзину
        time.sleep(1)
        cart = self.action.move_to_element((self.get_element(*MainPageLocators.GO_TO_CART_BUTTON)))
        cart.perform()
        time.sleep(1)
        self.is_element_clickable(self.get_element(*MainPageLocators.GO_TO_CART_BUTTON)).click()
        print("Click go to cart button")

    def click_continue_ordering_button(self):
        self.is_element_clickable(self.get_element(*MainPageLocators.CONTINUE_ORDERING_BUTTON)).click()
        print("Click continue ordering")

    def assert_price(self):
        self.assert_word(self.get_element(*MainPageLocators.ORDER_PRICE), "2 774 ₽")
        print("Order price is correct")
    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_enter_button()
        self.input_user_name("Dmitrii357")
        self.input_password("Vfhbyf357")
        self.click_login_button()
        self.assert_word(self.get_element(*MainPageLocators.AUTHORIZED_USER_ICON), "Dmitrii357")

    def choose_product(self):
        self.click_catalogue_button()
        self.click_motor_oil()
        self.click_brand_list()
        self.click_oil_brand()
        self.click_composition_list()
        self.click_composition()
        self.click_first_position()
        self.click_add_to_cart_button()
        self.click_close_fancybox_button()
        self.click_go_to_cart_button()
        self.click_continue_ordering_button()
        self.assert_price()
        self.get_screenshot()
        print("Теперь осталось нажать кнопку - 'Согласен, отпрваить заказ'(см. скриншот), но можно не буду ее нажимать, а то позвонят!")
        time.sleep(3)
