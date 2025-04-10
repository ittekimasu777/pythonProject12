from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_shipping_info(self, name, address, city, postal_code):
        self.driver.find_element(By.ID, "shipping_first_name").send_keys(name)
        self.driver.find_element(By.ID, "shipping_address_1").send_keys(address)
        self.driver.find_element(By.ID, "shipping_city").send_keys(city)
        self.driver.find_element(By.ID, "shipping_postcode").send_keys(postal_code)

    def select_delivery_date(self):
        self.driver.find_element(By.ID, "delivery_date").click()
        self.driver.find_element(By.XPATH, "//td[@data-date='tomorrow']").click()

    def select_payment_on_delivery(self):
        self.driver.find_element(By.ID, "payment_method_cod").click()

    def place_order(self):
        self.driver.find_element(By.ID, "place_order").click()

    def is_order_confirmed(self):
        confirmation_message = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "order-confirmation"))
        )
        return "Ваш заказ принят" in confirmation_message.text
