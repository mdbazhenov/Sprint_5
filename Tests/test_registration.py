from locators import Locators
from helpers import Generators
from data import Urls, AuthData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_registration_valid_data(self, driver):
        driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.TO_REG_PAGE_LINK).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(AuthData.name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Generators().login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Generators().password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Urls.LOGIN_PAGE_URL))
        assert driver.current_url == Urls.LOGIN_PAGE_URL


    def test_registration_error_short_password(self, driver):
        driver.find_element(*Locators.TO_LOGIN_PAGE_BUTTON).click()
        driver.find_element(*Locators.TO_REG_PAGE_LINK).click()
        driver.find_element(*Locators.NAME_FIELD).send_keys(AuthData.name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Generators().login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(AuthData.invalid_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.INVALID_PASS_TEXT))
        assert driver.find_element(*Locators.INVALID_PASS_TEXT).text == 'Некорректный пароль'