import pytest

from pages.elements_page import ElementsPage


class TestElementsClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url='https://demoqa.com/checkbox'):
        self.elements_page = ElementsPage(browser, url)
        self.elements_page.open_page()


    def test_checkbox(self):
        self.elements_page.click_checkbox()
        assert self.elements_page.checkbox_is_present()
