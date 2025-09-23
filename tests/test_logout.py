from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config import TEST_USER
from urls import LOGIN_URL
from locators import (
    MainPageLocators,
    LoginPageLocators,
    ProfilePageLocators
)


class TestLogout:
    def test_logout_personal_account(self, driver):
        """Проверка выхода по кнопке «Выйти» в личном кабинете."""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ProfilePageLocators.EXIT_BUTTON
            )
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.LOGIN_BUTTON
            )
        )

        assert driver.current_url == LOGIN_URL
