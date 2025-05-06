import pytest
from selenium import webdriver
from data import Credentials
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from curl import *

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(home_page)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def authorized(driver):
    driver.find_element(*Locators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET))

    return driver

