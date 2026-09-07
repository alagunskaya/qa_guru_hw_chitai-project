from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    CITY_CONFIRM_BUTTON = (By.XPATH, "//button[contains(., 'Да, я здесь')]")
    COOKIE_CLOSE_BUTTON = (By.XPATH, "//button[contains(., 'Понятно, закрыть')]")
    PROMO_CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-popmechanic-close]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def close_popups(self):
        try:
            self.click_js(self.CITY_CONFIRM_BUTTON)
        except TimeoutException:
            print("Окно выбора города не появилось")
            pass
        try:
            #           self.wait.until(EC.presence_of_element_located(self.COOKIE_CLOSE_BUTTON))
            self.click_js(self.COOKIE_CLOSE_BUTTON)
        except TimeoutException:
            print("Cookie-баннер не найдено")
            pass

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def click_js(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)
