import allure
import pytest
from pages.main_page import MainPage


@allure.epic("UI Тесты chitai-gorod")
@allure.feature("Каталог")
class TestCatalog:

    @allure.title("Сортировка каталога по цене: от дешевых к дорогим")
    @pytest.mark.positive
    def test_sort_by_price_asc(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Открываем каталог и переходим к списку всех товаров"):
            main_page.open_catalog()
            main_page.click_see_all_products()
            main_page.wait_for_catalog_title()

        with allure.step("Открываем меню сортировки и выбираем 'Сначала дешевые'"):
            main_page.open_sorting()
            main_page.sort_by_price_asc()

        with allure.step("Ждем, пока кнопка сортировки покажет 'Сначала дешевые'"):
            main_page.wait_for_sort_button_text("Сначала дешевые")

        with allure.step("Собираем первые 10 цен"):
            prices = main_page.get_first_n_prices(10)

        with allure.step("Проверяем, что цены идут по возрастанию"):
            assert len(prices) == 10, f"Ожидалось 10 цен, получено {len(prices)}: {prices}"
            for i in range(len(prices) - 1):
                assert prices[i] <= prices[i + 1], f"{prices[i]} стоит перед {prices[i + 1]}. Все цены: {prices}"

    @allure.title("Сортировка каталога по цене: от дорогих к дешевым")
    @pytest.mark.positive
    def test_sort_by_price_desc(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Открываем каталог и переходим к списку всех товаров"):
            main_page.open_catalog()
            main_page.click_see_all_products()
            main_page.wait_for_catalog_title()

        with allure.step("Открываем меню сортировки и выбираем 'Сначала дорогие'"):
            main_page.open_sorting()
            main_page.sort_by_price_desc()
            main_page.wait_for_sort_button_text("Сначала дорогие")

        with allure.step("Собираем первые 10 цен"):
            prices = main_page.get_first_n_prices(10)

        with allure.step("Проверяем, что цены идут по убыванию"):
            assert len(prices) == 10, f"Ожидалось 10 цен, получено {len(prices)}: {prices}"
            for i in range(len(prices) - 1):
                assert prices[i] >= prices[i + 1], f"{prices[i]} стоит перед {prices[i + 1]}. Все цены: {prices}"
