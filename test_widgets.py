import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
action = ActionChains(browser)


def test_accordian():
    browser.get('https://demoqa.com/accordian')
    element = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((
        By.ID, "section2Heading")))
    element.click()
    time.sleep(2)
    element2 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((
        By.XPATH, '//*[@id="section2Content"]/p[1]')))
    assert 'Contrary' in element2.text


def test_auto_complete():
    browser.get('https://demoqa.com/auto-complete')
    element = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((
        By.ID, "autoCompleteMultipleInput")))
    element.send_keys('b')
    element.send_keys(Keys.ENTER)
    assert 'Blue' in browser.find_element(By.CLASS_NAME, "css-12jo7m5").text


def test_calendar():
    browser.get('https://demoqa.com/date-picker')
    browser.implicitly_wait(0.5)
    browser.find_element(By.ID, "datePickerMonthYearInput").click()
    browser.find_element(By.XPATH, "//div[contains(text(),'26')]").click()
    s = browser.find_element(By.ID, "datePickerMonthYearInput").get_attribute('value')
    assert '12/26/2022' in s


def test_slider():
    browser.get('https://demoqa.com/slider')
    element = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((
        By.CLASS_NAME, "range-slider__tooltip")))

    action.click_and_hold(element).move_by_offset(10, 0).release().perform()
    time.sleep(2)
    # else:
    # # highly likely a vertical slider
    # action.click_and_hold(sliderknob).move_by_offset(percent * height / 100, 0).release().perform()

