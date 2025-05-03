import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_registration_data

class TestRegistrationWithNewData:

    def test_registration(self,driver):
        name, email, password = generate_registration_data()
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 20).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))

        # Проверяем URL страницы входа
        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'