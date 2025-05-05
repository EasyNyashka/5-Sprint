import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials

def test_exit(driver):
    driver.find_element(*Locators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 50).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET))
    driver.find_element(*Locators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 30).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
    driver.find_element(*Locators.EXIT).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    current_url = driver.current_url
    assert "/login" in current_url
