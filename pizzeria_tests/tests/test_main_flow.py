import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.main_page import MainPage
from pages.cart_page import CartPage


@pytest.mark.usefixtures("driver")
def test_add_pizza_from_slider(driver):
    main_page = MainPage(driver)
    cart_page = CartPage(driver)

    main_page.open()

    # Прокрутка слайдера вправо
    main_page.scroll_slider(direction="right")

    # Добавление пиццы в корзину после прокрутки
    pizza_name = main_page.add_visible_pizza_to_cart(index=1)

    # Переход в корзину
    main_page.go_to_cart()

    # Проверка, что пицца есть в корзине
    assert cart_page.is_item_in_cart(pizza_name), f"Пицца '{pizza_name}' не найдена в корзине"
def test_pizza_description_page(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Получаем имя и переходим по картинке
    pizza_name = main_page.open_pizza_description_by_click()

    # Проверка, что название пиццы на странице совпадает
    from pages.product_page import ProductPage
    product_page = ProductPage(driver)
    displayed_name = product_page.get_product_name()

    assert pizza_name == displayed_name, f"Ожидалось: {pizza_name}, но показано: {displayed_name}"
def test_add_pizza_with_options_to_cart(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Переход на страницу описания пиццы
    pizza_name = main_page.open_pizza_description_by_click()

    from pages.product_page import ProductPage
    product_page = ProductPage(driver)

    # Выбор опции "Сырный борт"
    option_name = product_page.select_option("Сырный борт")

    # Добавление в корзину
    product_page.add_to_cart()

    # Переход в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Проверка наличия пиццы с выбранной опцией
    assert cart_page.is_item_in_cart(pizza_name), f"Пицца '{pizza_name}' не найдена в корзине"
    assert cart_page.is_option_in_cart(pizza_name, option_name), f"Опция '{option_name}' не отображается в корзине"
def test_cart_contains_all_selected_pizzas(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Добавим первую пиццу
    pizza_name1 = main_page.add_pizza_to_cart_by_index(0)

    # Пролистаем вправо и добавим ещё одну
    main_page.scroll_slider(direction="right")
    pizza_name2 = main_page.add_pizza_to_cart_by_index(2)

    # Переход в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Проверим, что обе пиццы есть
    assert cart_page.is_item_in_cart(pizza_name1), f"Пицца '{pizza_name1}' не найдена в корзине"
    assert cart_page.is_item_in_cart(pizza_name2), f"Пицца '{pizza_name2}' не найдена в корзине"
def test_update_pizza_quantity_in_cart(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Добавим пиццу
    pizza_name = main_page.add_pizza_to_cart_by_index(0)

    # Перейдём в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Установим количество 2
    cart_page.set_quantity(pizza_name, 2)

    # Нажмем "Обновить корзину"
    cart_page.update_cart()

    # Проверим, что обновилось
    quantity = cart_page.get_quantity(pizza_name)
    assert quantity == 2, f"Ожидалось количество 2, но получено {quantity}"
def test_remove_pizza_from_cart(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Добавим пиццу
    pizza_name = main_page.add_pizza_to_cart_by_index(1)

    # Перейдём в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Удалим пиццу
    cart_page.remove_item(pizza_name)

    # Проверим, что она исчезла
    assert not cart_page.is_item_in_cart(pizza_name), f"Пицца '{pizza_name}' всё ещё в корзине"
def test_filter_desserts_by_price(driver):
    main_page = MainPage(driver)
    main_page.open()

    main_page.go_to_menu()

    from pages.menu_page import MenuPage
    menu_page = MenuPage(driver)

    # Выбираем "Десерты"
    menu_page.select_category("Десерты")

    # Применяем фильтр по цене
    menu_page.filter_by_max_price(135)

    # Проверим, что все десерты ≤ 135 рублей
    prices = menu_page.get_all_item_prices()
    for price in prices:
        assert price <= 135, f"Найден десерт с ценой {price}, что больше 135₽"
def test_add_filtered_dessert_to_cart(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Идём в меню и выбираем категорию "Десерты"
    main_page.go_to_menu()

    from pages.menu_page import MenuPage
    menu_page = MenuPage(driver)
    menu_page.select_category("Десерты")
    menu_page.filter_by_max_price(135)

    # Добавим первый попавшийся десерт
    dessert_name = menu_page.add_first_visible_product_to_cart()

    # Перейдём в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Проверим, что десерт в корзине
    assert cart_page.is_item_in_cart(dessert_name), f"Десерт '{dessert_name}' не найден в корзине"
import time
import random
import string

def generate_random_user():
    username = "test_" + ''.join(random.choices(string.ascii_lowercase, k=5))
    email = f"{username}@example.com"
    password = "Test12345!"
    return username, email, password

def test_registration_flow(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Идём в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Нажимаем "Оформить заказ"
    cart_page.proceed_to_checkout()

    # Ожидается редирект на авторизацию → переходим в "Мой аккаунт"
    main_page.go_to_my_account()

    from pages.account_page import AccountPage
    account_page = AccountPage(driver)

    # Генерируем нового пользователя
    username, email, password = generate_random_user()

    # Регистрируемся
    account_page.register(username, email, password)

    # Проверяем, что залогинены
    assert account_page.is_logged_in(), "Пользователь не залогинен после регистрации"
def test_checkout_flow(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Идём в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Проверяем товары в корзине
    cart_page.verify_cart_items()

    # Переходим к оформлению заказа
    cart_page.proceed_to_checkout()

    from pages.checkout_page import CheckoutPage
    checkout_page = CheckoutPage(driver)

    # Вводим данные доставки
    checkout_page.enter_shipping_info("Андрей", "ул. Пицца, 1", "Москва", "123456")

    # Выбираем дату на завтра
    checkout_page.select_delivery_date()

    # Выбираем оплату при доставке
    checkout_page.select_payment_on_delivery()

    # Подтверждаем заказ
    checkout_page.place_order()

    # Проверяем подтверждение заказа
    assert checkout_page.is_order_confirmed(), "Заказ не был подтверждён!"
def test_checkout_flow(driver):
    main_page = MainPage(driver)
    main_page.open()

    # Идём в корзину
    main_page.go_to_cart()

    from pages.cart_page import CartPage
    cart_page = CartPage(driver)

    # Проверяем товары в корзине
    cart_page.verify_cart_items()

    # Переходим к оформлению заказа
    cart_page.proceed_to_checkout()

    from pages.checkout_page import CheckoutPage
    checkout_page = CheckoutPage(driver)

    # Вводим данные доставки
    checkout_page.enter_shipping_info("Андрей", "ул. Пицца, 1", "Москва", "123456")

    # Выбираем дату на завтра
    checkout_page.select_delivery_date()

    # Выбираем оплату при доставке
    checkout_page.select_payment_on_delivery()

    # Подтверждаем заказ
    checkout_page.place_order()

    # Проверяем подтверждение заказа
    assert checkout_page.is_order_confirmed(), "Заказ не был подтверждён!"
