import allure
import pytest
from pages.main_page import MainPage


@allure.epic("chitai-gorod")
@allure.feature("Поиск")
class TestSearch:

    @allure.title("Поиск книги")
    @pytest.mark.positive
    def test_search_book(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно выбора города"):
            main_page.close_popups()

        search_query = "Гравити Фолз"

        with allure.step(f"Вводим в поиск запрос: '{search_query}'"):
            main_page.search(search_query)

        with allure.step("Проверяем, что URL содержит '/search?phrase='"):
            assert "/search?phrase=" in driver.current_url, f"Ожидался URL с '/search?phrase=', получен: {driver.current_url}"

        with allure.step("Проверяем заголовок страницы 'Результаты поиска'"):
            title_text = main_page.get_search_title()
            assert "Результаты поиска" in title_text, f"Ожидался 'Результаты поиска', получен '{title_text}'"

    @allure.title("Проверка поиска с пустым запросом")
    @pytest.mark.positive
    def test_empty_search(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Нажимаем на кнопку поиска без ввода текста"):
            main_page.click_element(main_page.SEARCH_BUTTON)

        with allure.step("Проверяем, что URL остался прежним"):
            assert "/search?phrase=" not in driver.current_url, "Поиск сработал, хотя запрос пустой"

    @allure.title("Проверка поиска несуществующего товара")
    @pytest.mark.positive
    def test_search_no_results(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Вводим несуществующий запрос"):
            main_page.search("Wrongdfghjklrequests")

        with allure.step("Проверяем, что заголовок содержит 'Не принес результатов'"):
            title_text = main_page.get_search_title()
            assert "не принес результатов" in title_text, f"Ожидался текст 'Не принес результатов', получен: {title_text}"
