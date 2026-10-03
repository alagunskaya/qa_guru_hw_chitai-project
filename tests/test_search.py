import allure
import pytest
from pages.main_page import MainPage


@allure.epic("UI Тесты chitai-gorod")
@allure.feature("Поиск")
class TestSearch:

    @allure.title("Поиск книги: проверка наличия релевантных результатов")
    @pytest.mark.positive
    def test_search_book(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно выбора города и Cookie-баннер"):
            main_page.close_popups()

        search_query = "Гарри Поттер"

        with allure.step(f"Вводим в поиск запрос: '{search_query}'"):
            main_page.search(search_query)

        with allure.step("Проверяем, что появились карточки товаров"):
            titles = main_page.get_all_product_titles()
            print(f"\nНайдено товаров: {len(titles)}")
            print(f"Первые 3: {titles[:3]}")
            assert len(titles) > 0, "Результаты поиска пусты"

        with allure.step(f"Проверяем, что в названиях товаров есть '{search_query}'"):
            found = any(search_query.lower() in title.lower() for title in titles)
            assert found, f"Ни один товар не содержит '{search_query}'. Найдены: {titles[:3]}"

    @allure.title("Поиск несуществующего товара")
    @pytest.mark.positive
    def test_search_no_results(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        query = "wrongdfghjklrequests"

        with allure.step(f"Вводим несуществующий запрос: '{query}'"):
            main_page.search(query)

        with allure.step("Проверяем, что заголовок сообщает об отсутствии результатов"):
            title_text = main_page.get_search_title()
            assert "не принес результатов" in title_text, f"Ожидалось сообщение 'не принес результатов', получено: '{title_text}'"

        with allure.step("Проверяем, что показан блок 'Похоже на то, что вы ищете'"):
            assert main_page.is_similar_results_visible(), "Блок 'Похоже на то, что вы ищете' не отображается"

        with allure.step(f"Проверяем, что в похожих товарах нет '{query}'"):
            titles = main_page.get_all_product_titles()
            print(f"\nНайдено товаров: {len(titles)}")
            print(f"Первые 3: {titles[:3]}")

            assert len(titles) > 0, "Блок 'похожих' товаров пуст"
            found = any(query.lower() in t.lower() for t in titles)
            assert not found, f"Найден товар с '{query}'. Первые 3: {titles[:3]}"
