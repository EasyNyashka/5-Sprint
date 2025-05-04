import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_registration_data
from data import Credentials

class TestGoToPersonalAccount:

    def test_go_to_personal_account_unauthorized_user(self, driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*Locators.REGISTRATION).click()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/register"))
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET))
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        current_url = driver.current_url
        assert "/account" in current_url

    def test_go_to_personal_account_authorized_user(self, driver):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET))
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 30).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account"))
        current_url = driver.current_url
        assert "/account" in current_url

