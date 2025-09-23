from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import TEST_USER
from urls import PERSONAL_ACCOUNT_URL, BASE_URL
from locators import (
    MainPageLocators,
    LoginPageLocators,
    ProfilePageLocators
)


class TestPersonalAccount:
    def test_personal_account_button(self, driver):
        """Проверить переход в личный кабинет по клику на «Личный кабинет»"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                LoginPageLocators.LOGIN_BUTTON
            )
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                ProfilePageLocators.PROFILE_LINK
            )
        )
        assert driver.current_url == PERSONAL_ACCOUNT_URL

    def test_personal_account_constructor_button(self, driver):
        """Проверить переход в личный кабинет по клику на «Конструктор»"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                LoginPageLocators.LOGIN_BUTTON
            )
        ).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                ProfilePageLocators.CONSTRUCT_BUTTON
            )
        ).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.MAKE_ORDER_BUTTON
            )
        )
        assert driver.current_url == BASE_URL

    def test_personal_account_constructor_logo(self, driver):
        """Проверить переход в личный кабинет по клику на логотип Stellar Burgers"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                LoginPageLocators.LOGIN_BUTTON
            )
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(
                ProfilePageLocators.LOGO_LINK
            )
        ).click()

        assert driver.current_url == BASE_URL
