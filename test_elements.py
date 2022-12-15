from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import os

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://demoqa.com/elements')
action = ActionChains(browser)


def test_radiobutton():
    element = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((
        By.XPATH, "//span[contains(text(),'Radio Button')]")))
    element.click()
    element1 = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((
        By.CSS_SELECTOR, "[for*='yesRadio']")))
    element1.click()
    el = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((
        By.CLASS_NAME, "text-success")))
    assert 'Yes' in el.text


def test_web_tables():
    browser.get('https://demoqa.com/buttons')
    element1 = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((
        By.ID, "doubleClickBtn")))
    element1.click()
    action.double_click(element1).perform()
    element2 = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((
        By.ID, "doubleClickMessage")))
    assert 'You have done a double click' in element2.text
    element3 = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((
        By.ID, "rightClickBtn")))
    action.context_click(element3).perform()
    element4 = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((
        By.ID, "rightClickMessage")))
    assert 'You have done a right click' in element4.text


def test_upload_and_download():
    browser.get('https://demoqa.com/upload-download')
    browser.find_element(By.ID, "uploadFile").send_keys('/Users/kate/Downloads/image_2022-12-07_09-24-12.png')
    assert "C:\\fakepath\\" in browser.find_element(By.ID, "uploadedFilePath").text
    browser.find_element(By.ID, "downloadButton").click()


def test_dynamic_properties():
    browser.get('https://demoqa.com/dynamic-properties')
    element1 = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((
        By.ID, "enableAfter")))
    assert element1
    element2 = WebDriverWait(browser, 10).until(ec.presence_of_element_located((
        By.ID, "visibleAfter")))
    assert element2


