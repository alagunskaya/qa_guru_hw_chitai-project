import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_TITLE = (By.CSS_SELECTOR, "h1.search-title__head")
    SEARCH_INPUT = (By.ID, "app-search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Найти']")
    SIMILAR_RESULTS_TITLE = (By.CSS_SELECTOR, "h3.search-stub-similar__header")

    CATALOG_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-header='catalog']")
    SEE_ALL_BUTTON = (By.CSS_SELECTOR, "p[data-testid-link-catalog-menu='seeAll']")
    CATALOG_TITLE = (By.CSS_SELECTOR, "h1.catalog-page__title")

    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, "div.product-card__caption a")
    BUY_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-mini-product-card='canBuy']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-mini-product-card='inCart']")
    CART_TITLE = (By.CSS_SELECTOR, "h1.cart-page__title")
    CART_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-header='cart']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product-detail-page__title, h1.product-title__title")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "div.product-cart-title__head")
    CART_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div.ui-alert__title")
    REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-cart='removeProduct']")

    SORTING_BUTTON = (By.CSS_SELECTOR, "div.app-catalog-sorting")
    SORT_BY_PRICE_ASC = (By.CSS_SELECTOR, "div[data-testid-item-sort-catalog='priceAsc']")
    SORT_BY_PRICE_DESC = (By.CSS_SELECTOR, "div[data-testid-item-sort-catalog='priceDesc']")
    PRODUCT_PRICES = (By.CSS_SELECTOR, "span.product-mini-card-price__price.product-mini-card-price__price--reverse")

    def open(self):
        self.driver.get("https://www.chitai-gorod.ru/")

    def get_search_title(self):
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_TITLE))
        return self.get_text(self.SEARCH_TITLE)

    def open_catalog(self):
        self.click_element(self.CATALOG_BUTTON)

    def click_see_all_products(self):
        self.click_element(self.SEE_ALL_BUTTON)

    def get_catalog_title(self):
        self.wait.until(EC.visibility_of_element_located(self.CATALOG_TITLE))
        return self.get_text(self.CATALOG_TITLE)

    def search(self, query):
        self.type_text(self.SEARCH_INPUT, query)
        self.click_element(self.SEARCH_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_TITLE))

    def click_first_product(self):
        self.wait.until(EC.presence_of_element_located(self.FIRST_PRODUCT_CARD))
        self.scroll_to_element(self.FIRST_PRODUCT_CARD)
        self.click_js(self.FIRST_PRODUCT_CARD)
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLE))

    def click_buy_button(self):
        self.scroll_to_element(self.BUY_BUTTON)
        self.wait.until(EC.presence_of_element_located(self.BUY_BUTTON))
        self.click_js(self.BUY_BUTTON)

    def click_checkout_button(self):
        self.click_element(self.CHECKOUT_BUTTON)

    def get_cart_title(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_TITLE))
        return self.get_text(self.CART_TITLE)

    def wait_for_catalog_title(self):
        self.wait.until(EC.visibility_of_element_located(self.CATALOG_TITLE))

    def get_all_product_titles(self):
        self.wait.until(EC.presence_of_all_elements_located(self.FIRST_PRODUCT_CARD))
        elements = self.driver.find_elements(*self.FIRST_PRODUCT_CARD)
        return [el.text.strip() for el in elements if el.text.strip()]

    def is_similar_results_visible(self):
        # Блок 'Похоже на то, что вы ищете'
        return self.is_visible(self.SIMILAR_RESULTS_TITLE)

    def open_cart(self):
        self.click_element(self.CART_BUTTON)

    def wait_for_cart_title(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_TITLE))

    def open_sorting(self):
        self.click_element(self.SORTING_BUTTON)

    def sort_by_price_asc(self):
        self.click_element(self.SORT_BY_PRICE_ASC)

    def sort_by_price_desc(self):
        self.click_element(self.SORT_BY_PRICE_DESC)

    def get_first_n_prices(self, n=10):
        self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_PRICES))
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        prices = []
        for el in elements[:n]:
            text = el.text.replace("\xa0", "").replace(" ", "").replace("₽", "").strip()
            if text.isdigit():
                prices.append(int(text))
        return prices

    def wait_for_sort_button_text(self, expected_text):
        self.wait.until(EC.text_to_be_present_in_element(self.SORTING_BUTTON, expected_text))
        time.sleep(1)

    def get_cart_item_title(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEM_TITLE))
        return self.get_text(self.CART_ITEM_TITLE)

    def get_cart_empty_message(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_EMPTY_MESSAGE))
        return self.get_text(self.CART_EMPTY_MESSAGE)
