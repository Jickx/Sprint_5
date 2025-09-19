from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import BurgerIngredientLocators


class TestIngredientsTabs:
    def test_click_bun_tab_scrolls_to_buns(self, driver):
        """Проверка перехода в раздел Булки при нажатии вкладки Булки."""
        element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerIngredientLocators.BUNS_TAB)
        )

        ActionChains(driver).move_to_element(element).click().perform()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerIngredientLocators.BUNS_SECTION)
        )

        assert driver.find_element(*BurgerIngredientLocators.ACTIVE_TAB).text == "Булки"

    def test_click_sauce_tab_scrolls_to_sauces(self, driver):
        """Проверка перехода в раздел Соусы при нажатии вкладки Соусы."""
        element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerIngredientLocators.SAUCES_TAB)
        )

        ActionChains(driver).move_to_element(element).click().perform()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerIngredientLocators.SAUCES_SECTION)
        )

        assert driver.find_element(*BurgerIngredientLocators.ACTIVE_TAB).text == "Соусы"

    def test_click_filling_tab_scrolls_to_fillings(self, driver):
        """Проверка перехода в раздел Начинки при нажатии вкладки Начинки."""
        element = WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerIngredientLocators.FILLINGS_TAB)
        )

        ActionChains(driver).move_to_element(element).click().perform()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(BurgerIngredientLocators.FILLINGS_SECTION)
        )

        assert driver.find_element(*BurgerIngredientLocators.ACTIVE_TAB).text == "Начинки"
