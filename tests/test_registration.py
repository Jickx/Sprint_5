from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import BASE_URL

from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators


class TestRegistration:

    def test_success_registration(self, valid_user, driver):
        """Проверка успешной регистрации."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(valid_user['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(valid_user['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_user['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.LOGIN_BUTTON
            )
        )
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(valid_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(valid_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == BASE_URL

    def test_registration_invalid_password_error(self, invalid_user, driver):
        """Проверка регистрации с невалидным паролем 5 символов."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(invalid_user['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(invalid_user['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(invalid_user['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                RegisterPageLocators.ERROR_MESSAGE
            )
        ).text

        assert error_message == 'Некорректный пароль'

    def test_registration_empty_name_error(self, valid_user, driver):
        """Проверка регистрации с пустым полем имени."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('')
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(valid_user['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_user['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                RegisterPageLocators.ERROR_MESSAGE
            )
        ).text

        assert error_message == 'Некорректное имя'

    def test_registration_empty_email_error(self, valid_user, driver):
        """Проверка регистрации с пустым полем пароля."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(valid_user['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys('')
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_user['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                RegisterPageLocators.ERROR_MESSAGE
            )
        ).text

        assert error_message == 'Некорректный email'

    def test_registration_existing_user_error(self, existing_user, driver):
        """Проверка регистрации при вводе существующего пользователя."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(existing_user['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                RegisterPageLocators.ERROR_MESSAGE
            )
        ).text

        assert error_message == 'Такой пользователь уже существует'
