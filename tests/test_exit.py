import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from curl import *

def test_exit(driver):
    driver.find_element(*Locators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 50).until(EC.url_to_be(login_page))
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET))
    driver.find_element(*Locators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 30).until(EC.url_to_be(account_page))
    driver.find_element(*Locators.EXIT).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(login_page))
    current_url = driver.current_url
    assert login_page in current_url
