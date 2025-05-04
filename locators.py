from selenium.webdriver.common.by import By

class Locators:

# Главная страница
    # Вход через Личный кабинет
    PERSONAL_CABINET = (By.LINK_TEXT, "Личный Кабинет")
    # Вход через кнопку Войти в аккаунт
    LOGIN_TO_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Страница Login
    # Кнопка "Войти"
    LOGIN = (By.XPATH, "//button[text()='Войти']")
    # Кнопка для входа на страницу регистрации
    REGISTRATION = (By.LINK_TEXT, "Зарегистрироваться")
    # Ссылка "Восстановить пароль"
    RECOVER_PASSWORD = (By.LINK_TEXT, "Восстановить пароль")
    # Выход на главную страницу
    EXIT_TO_THE_MAIN_PAGE = (By.XPATH, "//a[@class='active']")

# Страница регистрации
    # Поле "Имя"
    NAME = (By.NAME , "name")
    # Поле "Email"
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    # Поле "Пароль"
    PASSWORD = (By.NAME, "Пароль")
    # Кнопка для регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ENTRY = (By.LINK_TEXT, "Вход")
    # Сообщение "Некорректный пароль"
    ERROR_REGISTRATION = (By.XPATH, "//p[@class='input__error text_type_main-default']")
    # Кнопка "Войти"
    REGISTERED_LOGIN = (By.XPATH, "//a[@class='Auth_link__1fOlj']")

# Страница восстановления пароля
   # Ввод email
    EMAIL_FOR_RECOVERY = (By.XPATH, "//input[@class='text input__textfield text_type_main-default']")
    # Кнопка "Восстановить"
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
