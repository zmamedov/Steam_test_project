import allure
from allure_commons.types import Severity

from steam_ui_test_project.pages.main_page import main_page
from steam_ui_test_project.pages.login_page import login_page


@allure.epic('Login page')
@allure.feature('Elements on login page')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestLoginPage:
    @allure.title('Open login page')
    @allure.story('Login button')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_open_login_page(self):
        main_page.open_main_page()

        login_page.click_on_login()

        login_page.check_login_page()
