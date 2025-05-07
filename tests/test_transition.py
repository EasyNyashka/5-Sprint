import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Credentials
from curl import *

class TestTransiting:

    @pytest.mark.parametrize("locator", [Locators.CONSTRUCTOR, Locators.LOGO])
    def test_transition_from_personal_cabinet(dself, driver, locator):
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_page))
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.PERSONAL_CABINET))
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*locator).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(home_page))
        assert driver.current_url == home_page

