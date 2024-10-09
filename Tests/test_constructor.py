from locators import Locators
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestToConstructor:

    def test_to_constructor_by_button(self, login, driver):
        driver.find_element(*Locators.TO_ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        print("yay!")
        driver.find_element(*Locators.TO_CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
        assert driver.current_url == Urls.MAIN_PAGE_URL
        print("ura")

    def test_to_constructor_by_logo(self, login, driver):
        driver.find_element(*Locators.TO_ACCOUNT_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Locators.TO_ORDER_BUTTON))
        assert driver.current_url == Urls.MAIN_PAGE_URL


class TestConstructorSections:

    def test_to_sauces_section(self, driver):
        driver.find_element(*Locators.SAUCES_SECTION).click()
        section = driver.find_element(*Locators.SAUCES_SECTION).get_attribute('class')
        assert 'current' in section

    def test_to_buns_section(self, driver):
        driver.find_element(*Locators.SAUCES_SECTION).click()
        driver.find_element(*Locators.BUNS_SECTION).click()
        section = driver.find_element(*Locators.BUNS_SECTION).get_attribute('class')
        assert 'current' in section

    def test_to_toppings_section(self, driver):
        driver.find_element(*Locators.TOPPINGS_SECTION).click()
        section = driver.find_element(*Locators.TOPPINGS_SECTION).get_attribute('class')
        assert 'current' in section