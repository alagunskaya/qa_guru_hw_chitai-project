import time

import allure
import pytest
from pages.main_page import MainPage


@allure.epic("UI Тесты chitai-gorod")
@allure.feature("Корзина")
class TestCart:

    @allure.title("Добавление книги в корзину")
    @pytest.mark.positive
    def test_add_book_to_cart(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно выбора города"):
            main_page.close_popups()

        with allure.step("Открываем каталог и переходим к списку всех товаров"):
            main_page.open_catalog()
            main_page.click_see_all_products()


        with allure.step("Кликаем по первой книге в каталоге"):
            main_page.click_first_product()

        with allure.step("Нажимаем кнопку 'Купить'"):
            main_page.click_buy_button()

        with allure.step("Нажимаем кнопку 'Оформить'"):
            main_page.click_checkout_button()

        with allure.step("Проверяем, что открылась корзина с заголовком 'Корзина'"):
            cart_title = main_page.get_cart_title()
            assert cart_title == "Корзина", f"Ожидался заголовок 'Корзина', получен '{cart_title}'"