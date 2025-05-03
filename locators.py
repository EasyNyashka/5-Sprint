from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_CABINET = (By.LINK_TEXT, "Личный Кабинет")
    LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    REGISTRATION = (By.LINK_TEXT, "Зарегистрироваться")
#Страница регистрации
    # Поле "Имя"
    NAME = (By.NAME , "name")
    # Поле "Email"
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    # Поле "Пароль"
    PASSWORD = (By.NAME, "Пароль")

    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ENTRY = (By.LINK_TEXT, "Вход")
    ERROR_REGISTRATION = (By.XPATH, "//p[@class='input__error text_type_main-default']")