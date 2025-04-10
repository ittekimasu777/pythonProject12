from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://pizzeria.skillbox.cc/"
        self.slider_right_arrow = (By.CSS_SELECTOR, ".slick-next")
        self.pizza_cards = (By.CSS_SELECTOR, ".dish-card")

    def open(self):
        self.driver.get(self.url)

    def scroll_slider(self, direction="right"):
        if direction == "right":
            self.driver.find_element(*self.slider_right_arrow).click()
            time.sleep(1)  # подождать анимацию

    def add_visible_pizza_to_cart(self, index=0):
        cards = self.driver.find_elements(*self.pizza_cards)
        target = cards[index]
        ActionChains(self.driver).move_to_element(target).perform()

        add_button = target.find_element(By.XPATH, ".//button[contains(text(), 'В корзину')]")
        pizza_name = target.find_element(By.CLASS_NAME, "dish-card__title").text
        add_button.click()
        return pizza_name

    def go_to_cart(self):
        cart_button = self.driver.find_element(By.CSS_SELECTOR, ".header__cart")
        cart_button.click()
    def open_pizza_description_by_click(self, index=0):
        cards = self.driver.find_elements(*self.pizza_cards)
        target = cards[index]
        pizza_name = target.find_element(By.CLASS_NAME, "dish-card__title").text
        pizza_image = target.find_element(By.TAG_NAME, "img")
        pizza_image.click()
        return pizza_name
    def add_pizza_to_cart_by_index(self, index):
        cards = self.driver.find_elements(*self.pizza_cards)
        pizza = cards[index]
        name = pizza.find_element(By.CLASS_NAME, "dish-card__title").text

        # Наводим курсор, чтобы появилась кнопка
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.driver).move_to_element(pizza).perform()

        pizza.find_element(By.CLASS_NAME, "dish-card__button").click()
        return name

    def scroll_slider(self, direction="right"):
        arrow_class = "slider-arrow--next" if direction == "right" else "slider-arrow--prev"
        self.driver.find_element(By.CLASS_NAME, arrow_class).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "header__cart").click()
    def go_to_menu(self):
        self.driver.find_element(By.LINK_TEXT, "Меню").click()
    def go_to_my_account(self):
        self.driver.find_element(By.LINK_TEXT, "Мой аккаунт").click()
