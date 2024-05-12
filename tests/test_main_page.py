import allure
from allure_commons.types import Severity

from steam_ui_test_project.pages.main_page import main_page


@allure.feature('Elements on main page')
@allure.epic('Main page')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestMainPage:

    @allure.title('Switch on tab "Community"')
    @allure.story('Tabs')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_switch_tab(self):
        main_page.open_main_page()

        main_page.switch_navigation_tab(tab_name='COMMUNITY')

        main_page.check_community_tab_title()

    @allure.title('Change the language on the main page to French')
    @allure.story('Global actions')
    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'zmamedov')
    def test_change_language(self):
        main_page.open_main_page()

        main_page.click_on_list_of_lang()
        main_page.choose_lang(lang="french")

        main_page.check_french_lang_on_page()
