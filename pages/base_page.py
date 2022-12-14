import logging
from typing import Tuple

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    LOGGER = logging.getLogger(__name__)
    CHECKBOX_BUTTON = (By.CSS_SELECTOR, '.rct-icon.rct-icon-uncheck')
    TEXT_CONFIRM_CHECKBOX = (By.XPATH, "//span[contains(text(),'You have selected :')]")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        try:
            self.browser.get(self.url)
        except Exception as e:
            self.LOGGER.error(f"tException: {e}")

    def wait_for_url_to_be(self, url: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(ec.url_to_be(url))
            return True
        except Exception as error:
            self.LOGGER.error(f"Exception: {error}")

    def page_title_is(self, title: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(ec.title_is(title))
            return True
        except Exception as e:
            self.LOGGER.error(f"Exception: {e}")

    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.element_to_be_clickable(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_not_present(self, locator: Tuple, timeout=5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until_not(
                ec.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_visible(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def element_is_present(self, locator: Tuple, timeout: int = 5) -> bool:
        try:
            self.wait_until_visible(locator, timeout)
            return True
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def page_is_open(self, url):
        try:
            self.wait_for_url_to_be(url)
            return True
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")
            return False

    def elements_are_present(self, locator, timeout: int = 5):
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.presence_of_all_elements_located(locator)
            )
        except Exception as e:
            self.LOGGER.error(f"Exception: {e}")




