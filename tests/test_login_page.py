import allure
from allure_commons.types import Severity

from qa_guru_diplom_ui.pages.main_page import main_page
from qa_guru_diplom_ui.pages.login_page import login_page


@allure.feature('Login page')
@allure.epic('Login page')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestLoginPage:
    @allure.title('Open login page')
    @allure.story('Login page')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_open_login_page(self):
        main_page.open_main_page()

        login_page.click_on_login()

        login_page.check_login_page()
