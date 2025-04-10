from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def is_item_in_cart(self, name):
        items = self.driver.find_elements(By.CLASS_NAME, "cart-item__title")
        return any(name in item.text for item in items)
    def is_option_in_cart(self, pizza_name, option_name):
        items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "cart-item__title").text
            if pizza_name in name:
                return option_name in item.text
        return False
    def is_item_in_cart(self, pizza_name):
        items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "cart-item__title").text
            if pizza_name in name:
                return True
        return False
    def set_quantity(self, pizza_name, quantity):
        items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
        for item in items:
            title = item.find_element(By.CLASS_NAME, "cart-item__title").text
            if pizza_name in title:
                qty_input = item.find_element(By.CSS_SELECTOR, "input.qty")
                qty_input.clear()
                qty_input.send_keys(str(quantity))
                return
        raise Exception(f"Пицца '{pizza_name}' не найдена в корзине")

    def update_cart(self):
        self.driver.find_element(By.NAME, "update_cart").click()

    def get_quantity(self, pizza_name):
        items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
        for item in items:
            title = item.find_element(By.CLASS_NAME, "cart-item__title").text
            if pizza_name in title:
                qty_input = item.find_element(By.CSS_SELECTOR, "input.qty")
                return int(qty_input.get_attribute("value"))
        raise Exception(f"Пицца '{pizza_name}' не найдена в корзине")
    def remove_item(self, pizza_name):
        items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
        for item in items:
            title = item.find_element(By.CLASS_NAME, "cart-item__title").text
            if pizza_name in title:
                remove_button = item.find_element(By.CLASS_NAME, "remove")
                remove_button.click()
                return
        raise Exception(f"Пицца '{pizza_name}' не найдена для удаления")
    def proceed_to_checkout(self):
        self.driver.find_element(By.CLASS_NAME, "checkout-button").click()
    def verify_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(items) > 0, "Корзина пуста"
        for item in items:
            product_name = item.find_element(By.CLASS_NAME, "product-name").text
            assert product_name != "", f"Товар без названия: {item}"
