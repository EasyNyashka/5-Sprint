import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials

class TestEntry:

    def test_valid_entry_via_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        assert driver.current_url

    def test_valid_entry_via_login_to_account(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 50).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        assert driver.current_url

    def test_valid_entry_via_recover_password(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/forgot-password"))
        current_url = driver.current_url
        assert "/forgot-password" in current_url

    def test_valid_entry_via_registration(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.REGISTERED_LOGIN).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        assert driver.current_url