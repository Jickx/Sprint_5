from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import PERSONAL_ACCOUNT_URL, BASE_URL
from locators import (
    MainPageLocators,
    LoginPageLocators,
    ProfilePageLocators
)


class TestPersonalAccount:
    def test_personal_account_button(self, existing_user, driver):
        """Проверить переход в личный кабинет по клику на «Личный кабинет»"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ProfilePageLocators.PROFILE_LINK
            )
        )
        assert driver.current_url == PERSONAL_ACCOUNT_URL

    def test_personal_account_constructor_button(self, existing_user, driver):
        """Проверить переход в личный кабинет по клику на «Конструктор»"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ProfilePageLocators.CONSTRUCT_BUTTON
            )
        ).click()

        assert driver.current_url == BASE_URL

    def test_personal_account_constructor_logo(self, existing_user, driver):
        """Проверить переход в личный кабинет по клику на логотип Stellar Burgers"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(existing_user['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(existing_user['password'])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(
                ProfilePageLocators.LOGO_LINK
            )
        ).click()

        assert driver.current_url == BASE_URL
