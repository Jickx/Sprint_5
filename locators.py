from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # TODO
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']//following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти'] ")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']//following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']//following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")
