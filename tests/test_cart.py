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

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Открываем каталог и переходим к списку всех товаров"):
            main_page.open_catalog()
            main_page.click_see_all_products()
            main_page.wait_for_catalog_title()

        with allure.step("Запоминаем название первой книги в каталоге"):
            expected_title = main_page.get_text(main_page.FIRST_PRODUCT_CARD)
            assert expected_title, "Не удалось получить название книги"

        with allure.step(f"Кликаем по книге: '{expected_title}'"):
            main_page.click_first_product()

        with allure.step("Нажимаем кнопку 'Купить'"):
            main_page.click_buy_button()

        with allure.step("Нажимаем кнопку 'Оформить'"):
            main_page.click_checkout_button()

        with allure.step("Проверяем, что в корзине именно эта книга"):
            cart_title = main_page.get_cart_item_title()
            print(f"\nОжидали в корзине: '{expected_title}'")
            print(f"Фактически в корзине: '{cart_title}'")

            assert cart_title == expected_title, f"Ожидалась книга '{expected_title}', в корзине '{cart_title}'"

    @allure.title("Удаление товара из корзины")
    @pytest.mark.positive
    def test_remove_book_from_cart(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            main_page.open()

        with allure.step("Закрываем окно города и Cookie-баннер"):
            main_page.close_popups()

        with allure.step("Открываем каталог и переходим к списку всех товаров"):
            main_page.open_catalog()
            main_page.click_see_all_products()
            main_page.wait_for_catalog_title()

        with allure.step("Добавляем первую книгу в корзину"):
            main_page.click_first_product()
            main_page.click_buy_button()
            main_page.click_checkout_button()
            main_page.wait_for_cart_title()

        with allure.step("Нажимаем кнопку удаления товара"):
            main_page.click_element(main_page.REMOVE_FROM_CART_BUTTON)

        with allure.step("Проверяем, что появилось сообщение о пустой корзине"):
            message = main_page.get_cart_empty_message()
            assert "Вы не выбрали ни одного товара" in message, f"Ожидалось сообщение о пустой корзине, получено: '{message}'"
