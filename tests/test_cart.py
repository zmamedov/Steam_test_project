import allure
from allure_commons.types import Severity

from steam_ui_test_project.pages.main_page import main_page
from steam_ui_test_project.pages.search_page import search_page
from steam_ui_test_project.pages.cart_page import cart_page


@allure.epic('Cart')
@allure.feature('Products in cart')
@allure.link('https://store.steampowered.com/', name='Steam')
class TestCart:
    @allure.title('Add game to the cart')
    @allure.story('Add game')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_add_game_to_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_game_in_search(game_name="Manor Lords")
        search_page.click_on_first_game_in_search_row()
        cart_page.add_game_to_cart()
        cart_page.move_to_cart()

        cart_page.check_game_in_cart(game_name="Manor Lords")

    @allure.title('Remove game from the cart')
    @allure.story('Remove game')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_remove_game_from_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_game_in_search(game_name="Manor Lords")
        search_page.click_on_first_game_in_search_row()
        cart_page.add_game_to_cart()
        cart_page.move_to_cart()
        cart_page.remove_game_from_cart()

        cart_page.check_empty_cart()

    @allure.title('Full clear of the cart')
    @allure.story('Clear cart')
    @allure.tag('web')
    @allure.severity(Severity.CRITICAL)
    @allure.label('owner', 'zmamedov')
    def test_clear_cart(self):
        main_page.open_main_page()

        search_page.click_on_search()
        search_page.find_game_in_search(game_name="Manor Lords")
        search_page.click_on_first_game_in_search_row()
        cart_page.add_game_to_cart()
        cart_page.continue_buying()
        search_page.click_on_search()
        search_page.find_game_in_search(game_name="Europa Universalis IV")
        search_page.click_on_first_game_in_search_row()
        cart_page.add_game_to_cart()
        cart_page.move_to_cart()
        cart_page.clear_cart()

        cart_page.check_empty_cart()
