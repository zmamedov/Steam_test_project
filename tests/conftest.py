import os

import pytest
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene import browser

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "122.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    driver = webdriver.Remote(
        command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = 'https://store.steampowered.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()
