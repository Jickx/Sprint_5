from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка перехода в личный кабинет
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка оформления заказа
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа в аккаунт


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//following-sibling::input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']//following-sibling::input")  # Поле ввода пароля
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти'] ")  # Кнопка входа
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # Ссылка на страницу регистрации
    RECOVER_LINK = (By.XPATH, "//a[@href='/forgot-password']")  # Ссылка на восстановление пароля


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']//following-sibling::input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//following-sibling::input")  # Поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']//following-sibling::input")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка регистрации
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")  # Сообщение об ошибке ввода
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Ссылка на страницу входа


class RecoveryPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # Ссылка на страницу входа с восстановления пароля


class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")  # Ссылка на профиль пользователя
    CONSTRUCT_BUTTON = (By.XPATH, "//li/a[@href='/']")  # Кнопка перехода к конструктору бургеров
    LOGO_LINK = (By.XPATH, "//div/a[@href='/']")  # Ссылка-логотип на главную страницу
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода из аккаунта


class BurgerIngredientLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Вкладка "Булки"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Вкладка "Соусы"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Вкладка "Начинки"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")  # Секция "Булки"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")  # Секция "Соусы"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")  # Секция "Начинки"
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span")  # Активная вкладка
