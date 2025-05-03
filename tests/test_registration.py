import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_registration_data
from data import Credentials

class TestRegistrationWithNewData:

    def test_registration_valid_data(self,driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        current_url = driver.current_url
        assert "/login" in current_url

    def test_registration_invalid_name(self, driver, locaNone):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.NAME).send_keys('')
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/register"))
        current_url = driver.current_url
        assert "/register" in current_url

    def test_registration_invalid_email(self,driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys('Elena.ru')
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/register"))
        current_url = driver.current_url
        assert "/register" in current_url

    def test_registration_invalid_password(self,driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('1w1')
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 15).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/register"))
        current_url = driver.current_url
        assert "/register" in current_url

    def test_creation_existing_account(self, driver):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        error_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.ERROR_REGISTRATION))
        assert error_element.text == 'Такой пользователь уже существует'