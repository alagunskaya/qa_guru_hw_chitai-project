from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    SEARCH_TITLE = (By.CSS_SELECTOR, "h1.search-title__head")
    SEARCH_INPUT = (By.ID, "app-search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Найти']")

    CATALOG_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-header='catalog']")
    SEE_ALL_BUTTON = (By.CSS_SELECTOR, "p[data-testid-link-catalog-menu='seeAll']")
    CATALOG_TITLE = (By.CSS_SELECTOR, "h1.catalog-page__title")

    FIRST_PRODUCT_CARD = (By.CSS_SELECTOR, "div.product-card__caption a")
    BUY_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-mini-product-card='canBuy']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button[data-testid-button-mini-product-card='inCart']")
    CART_TITLE = (By.CSS_SELECTOR, "h1.cart-page__title")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "h1.product-detail-page__title")

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
        self.wait.until(EC.presence_of_element_located(self.BUY_BUTTON))
        self.click_js(self.BUY_BUTTON)

    def click_checkout_button(self):
        self.click_element(self.CHECKOUT_BUTTON)

    def get_cart_title(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_TITLE))
        return self.get_text(self.CART_TITLE)
