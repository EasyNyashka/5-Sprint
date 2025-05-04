from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import generate_registration_data
from data import Credentials

class GoToPersonalAccount:

    def test_go_to_personal_account_unauthorized_user(self, driver):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*Locators.REGISTRATION).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        current_url = driver.current_url