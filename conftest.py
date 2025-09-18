from selenium import webdriver
from generators import UserGenerator
from config import BASE_URL, TEST_USER
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def valid_user():
    return UserGenerator.generate_user(valid_password=True)


@pytest.fixture
def invalid_user():
    return UserGenerator.generate_user(valid_password=False)

@pytest.fixture
def existing_user():
    return TEST_USER
