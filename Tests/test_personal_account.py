from locators import Locators
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestPersonalAccount:

    def test_to_personal_account(self, login, driver):
        driver.find_element(*Locators.TO_ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        assert driver.current_url == Urls.PERSONAL_ACCOUNT_URL

    def test_logout_from_personal_account_page(self, login, driver):
        driver.find_element(*Locators.TO_ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Urls.LOGIN_PAGE_URL))
        button_text = driver.find_element(*Locators.LOGIN_BUTTON).text
        assert button_text == 'Войти'