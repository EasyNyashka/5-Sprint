from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_CABINET = (By.LINK_TEXT, "Личный Кабинет")
    LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    REGISTRATION = (By.LINK_TEXT, "Зарегистрироваться")

    NAME = (By.NAME , "name")
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    PASSWORD = (By.NAME, "Пароль")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ENTRY = (By.LINK_TEXT, "Вход")