from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_locator = (By.CLASS_NAME, "product-title")

    def get_product_name(self):
        return self.driver.find_element(*self.name_locator).text
class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_locator = (By.CLASS_NAME, "product-title")
        self.option_list = (By.CSS_SELECTOR, ".product-addition__item")
        self.add_to_cart_button = (By.CSS_SELECTOR, ".product-controls__add-to-cart")

    def get_product_name(self):
        return self.driver.find_element(*self.name_locator).text

    def select_option(self, name):
        options = self.driver.find_elements(*self.option_list)
        for option in options:
            if name in option.text:
                option.click()
                return name
        raise Exception(f"Опция '{name}' не найдена")

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
