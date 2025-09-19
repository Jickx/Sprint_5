from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from urls import BASE_URL
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, RecoveryPageLocators


class TestLogin:
    def test_login_home_page_button(self, existing_user, driver):
        """Проверка входа по кнопке «Войти в аккаунт» на главной."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == BASE_URL

    def test_login_personal_account(self, existing_user, driver):
        """Проверка входа через кнопку «Личный кабинет»."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == BASE_URL

    def test_login_registration(self, existing_user, driver):
        """Проверка входа через кнопку в форме регистрации."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == BASE_URL

    def test_login_recovery(self, existing_user, driver):
        """Проверка входа через кнопку в форме восстановления пароля."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.RECOVER_LINK).click()
        driver.find_element(*RecoveryPageLocators.LOGIN_LINK).click()

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == BASE_URL
