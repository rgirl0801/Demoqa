import logging

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ElementsPage(BasePage):
    LOGGER = logging.getLogger(__name__)
    CHECKBOX_BUTTON = (By.CSS_SELECTOR, '.rct-icon.rct-icon-uncheck')
    RESULT_CHECKBOX = (By.XPATH, "//div[@id='result']")

    def click_checkbox(self):
        self.wait_until_clickable(self.CHECKBOX_BUTTON).click()

    def checkbox_is_present(self):
        self.wait_until_visible(self.RESULT_CHECKBOX)

