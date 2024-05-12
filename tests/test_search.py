import allure
from allure_commons.types import Severity

from steam_ui_test_project.pages.main_page import main_page
from steam_ui_test_project.pages.search_page import search_page


@allure.epic('Search')
@allure.feature('Search field')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestSearch:
    @allure.title('Find game via search field')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_search_field(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_game_in_search(game_name="Baldur's Gate 3")

        search_page.check_search_result(game_name="Baldur's Gate 3")
