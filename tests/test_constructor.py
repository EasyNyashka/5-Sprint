from time import sleep

import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor:
    def test_transition_to_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.SAUCES_SECTION)
        souces_sector = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.SAUCES_SECTION))
        assert souces_sector.text == "Соусы"

    def test_transition_to_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.FILLINGS_SECTION)
        fillings_sector = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.FILLINGS_SECTION))
        assert fillings_sector.text == "Начинки"

    def test_transition_to_buns(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUNS).click()
        buns_sector = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.BUNS_SECTION))
        assert buns_sector.text == "Булки"
