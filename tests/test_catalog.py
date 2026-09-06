import allure
import pytest
from pages.main_page import MainPage


@allure.epic("UI Тесты chitai-gorod")
@allure.feature("Каталог")
class TestCatalog:

    @allure.title("Просмотр всех товаров каталога")
    @pytest.mark.positive
    def test_view_all_books(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно выбора города"):
            main_page.close_popups()

        with allure.step("Кликаем кнопку 'Каталог'"):
            main_page.open_catalog()

        with allure.step("Выбираем 'Смотреть все товары'"):
            main_page.click_see_all_products()

        with allure.step("Проверяем заголовок страницы 'Книги'"):
            catalog_title = main_page.get_catalog_title()
            assert catalog_title == "Книги", f"Ожидался заголовок 'Книги', получен '{catalog_title}'"
