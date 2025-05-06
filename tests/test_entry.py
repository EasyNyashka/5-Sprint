import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from curl import *

class TestEntry:

    def test_valid_entry_via_personal_account(self, driver):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        assert driver.current_url

    def test_valid_entry_via_login_to_account(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        assert driver.current_url

    def test_valid_entry_via_recover_password(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(forgot_page))
        driver.find_element(*Locators.EMAIL_FOR_RECOVERY).send_keys(Credentials.email)
        driver.find_element(*Locators.RECOVER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(reset))
        current_url = driver.current_url
        assert reset in current_url

    def test_valid_entry_via_registration(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.REGISTERED_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        assert driver.current_url

    def test_entry_via_personal_account_invalid_email(self, driver):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys('Некорректный адрес')
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        current_url = driver.current_url
        assert login_page in current_url

    def test_entry_via_personal_account_invalid_password(self, driver):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys('123')
        driver.find_element(*Locators.LOGIN).click()
        error_text = driver.find_element(*Locators.ERROR_REGISTRATION).text
        assert 'Некорректный пароль' in error_text

    def test_entry_via_login_to_account_invalid_email(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys('Некорректный адрес')
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        current_url = driver.current_url
        assert login_page in current_url

    def test_entry_via_login_to_account_invalid_password(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys('123')
        driver.find_element(*Locators.LOGIN).click()
        error_text = driver.find_element(*Locators.ERROR_REGISTRATION).text
        assert 'Некорректный пароль' in error_text

    def test_entry_via_recover_password_invalid_email(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(forgot_page))
        driver.find_element(*Locators.EMAIL_FOR_RECOVERY).send_keys('Некорректный адрес')
        driver.find_element(*Locators.RECOVER_BUTTON).click()
        current_url = driver.current_url
        assert forgot_page in current_url

    def test_entry_via_registration_invalid_email(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.REGISTERED_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys('Некорректный адрес')
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        current_url = driver.current_url
        assert login_page in current_url

    def test_entry_via_registration_invalid_password(self, driver):
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.REGISTERED_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys('123')
        driver.find_element(*Locators.LOGIN).click()
        error_text = driver.find_element(*Locators.ERROR_REGISTRATION).text
        assert 'Некорректный пароль' in error_text

