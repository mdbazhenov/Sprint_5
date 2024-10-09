import pytest
from locators import Locators
from data import Urls, AuthData
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1280,800')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(AuthData.login)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(AuthData.password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
