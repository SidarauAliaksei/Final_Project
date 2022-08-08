import pytest
import allure
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    with allure.step('Initializing chromedriver'):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.maximize_window()
        browser.implicitly_wait(5)
        yield browser
    with allure.step('Closing browser'):
        browser.quit()
