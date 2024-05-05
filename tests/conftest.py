import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://store.steampowered.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()
