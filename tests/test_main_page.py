import allure
from allure_commons.types import Severity

from qa_guru_diplom_ui.pages.main_page import main_page


@allure.feature('Elements on main Page')
@allure.epic('Main page')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestMainPage:

    @allure.title('Switch on tab "Community"')
    @allure.story('Main page')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_switch_tab(self):
        main_page.open_main_page()

        main_page.switch_navigation_tab(tab_name='СООБЩЕСТВО')

        main_page.check_community_tab_title()

    @allure.title('Change language in main page on French')
    @allure.story('Main page')
    @allure.tag('web')
    @allure.severity(Severity.NORMAL)
    @allure.label('owner', 'zmamedov')
    def test_change_language(self):
        main_page.open_main_page()

        main_page.click_on_list_of_lang()
        main_page.choose_lang(lang="french")

        main_page.check_french_lang_on_page()
