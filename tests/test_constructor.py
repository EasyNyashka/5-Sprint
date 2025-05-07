import pytest
from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructor:
    def test_transition_to_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        active_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_SECTION))
        assert "current" in active_section.get_attribute("class")
        assert active_section.text == "Соусы"

    def test_transition_to_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        active_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_SECTION))
        assert "current" in active_section.get_attribute("class")
        assert active_section.text == "Начинки"

    def test_transition_to_buns(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUNS).click()
        active_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.ACTIVE_SECTION))
        assert "current" in active_section.get_attribute("class")
        assert active_section.text == "Булки"
