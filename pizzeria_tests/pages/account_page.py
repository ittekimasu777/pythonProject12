from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def register(self, username, email, password):
        self.wait.until(EC.element_to_be_clickable((By.ID, "reg_username"))).send_keys(username)
        self.driver.find_element(By.ID, "reg_email").send_keys(email)
        self.driver.find_element(By.ID, "reg_password").send_keys(password)
        self.driver.find_element(By.NAME, "register").click()

    def is_logged_in(self):
        try:
            logout_link = self.wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Выйти"))
            )
            return logout_link.is_displayed()
        except:
            return False
