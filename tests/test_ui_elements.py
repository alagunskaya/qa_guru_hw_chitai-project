import allure
import pytest
from pages.main_page import MainPage


@allure.epic("UI Тесты chitai-gorod")
@allure.feature("Элементы интерфейса")
class TestUIElements:

    @allure.title("Проверка наличия элементов в хедере']")
    @pytest.mark.positive
    def test_header_elements_are_visible(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Проверяем логотип"):
            assert main_page.is_visible(main_page.LOGO), "Логотип не виден"

        with allure.step("Проверяем кнопку Каталог"):
            assert main_page.is_visible(main_page.CATALOG_BUTTON), "Кнопка Каталог не видна"

        with allure.step("Проверяем строку поиска"):
            assert main_page.is_visible(main_page.SEARCH_INPUT), "Строка поиска не видна"

    @allure.title("Проверка наличия элементов в правой части хедера")
    @pytest.mark.positive
    def test_header_right_elements_are_visible(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Проверяем кнопку профиля"):
            assert main_page.is_visible(main_page.LOGIN_BUTTON), "Кнопка профиля не видна"

        with allure.step("Проверяем кнопку Заказы"):
            assert main_page.is_visible(main_page.ORDERS_BUTTON), "Кнопка Заказы не видна"

        with allure.step("Проверяем кнопку Мои книги"):
            assert main_page.is_visible(main_page.MY_BOOKS_BUTTON), "Кнопка Мои книги не видна"

        with allure.step("Проверяем кнопку Корзина"):
            assert main_page.is_visible(main_page.CART_BUTTON), "Кнопка Корзина не видна"
