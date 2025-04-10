from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_category(self, name):
        select = Select(self.wait.until(EC.visibility_of_element_located((By.NAME, "product_cat"))))
        select.select_by_visible_text(name)
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product")))

    def filter_by_max_price(self, max_price):
        slider = self.driver.find_element(By.CLASS_NAME, "price_slider")
        # Можно заменить на ползунки или напрямую установить значения через input
        # Если есть input-элементы для min/max:
        max_price_input = self.driver.find_element(By.CSS_SELECTOR, ".price_slider_amount input.max_price")
        max_price_input.clear()
        max_price_input.send_keys(str(max_price))
        self.driver.find_element(By.CSS_SELECTOR, ".price_slider_amount button").click()
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product")))

    def get_all_item_prices(self):
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, ".product .price")
        prices = []
        for el in price_elements:
            text = el.text.strip().replace("₽", "").replace(" ", "")
            try:
                prices.append(int(float(text)))
            except ValueError:
                continue
        return prices
    def add_first_visible_product_to_cart(self):
        products = self.driver.find_elements(By.CLASS_NAME, "product")
        for product in products:
            try:
                name = product.find_element(By.CLASS_NAME, "woocommerce-loop-product__title").text
                add_button = product.find_element(By.CLASS_NAME, "add_to_cart_button")
                add_button.click()
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "added_to_cart")))
                return name
            except:
                continue
        raise Exception("Не удалось найти десерт для добавления в корзину")
