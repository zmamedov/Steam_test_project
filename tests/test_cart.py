from qa_guru_diplom_ui.pages.main_page import main_page
from qa_guru_diplom_ui.pages.search_page import search_page
from qa_guru_diplom_ui.pages.cart_page import cart_page


def test_add_game_to_cart():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")
    search_page.click_on_first_game_in_search_row()
    cart_page.add_game_to_cart()
    cart_page.move_to_cart()

    cart_page.check_game_in_cart(game_name="Baldur's Gate 3")


def test_remove_game_from_cart():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")
    search_page.click_on_first_game_in_search_row()
    cart_page.add_game_to_cart()
    cart_page.move_to_cart()
    cart_page.remove_game_from_cart()

    cart_page.check_empty_cart()


def test_clear_cart():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")
    search_page.click_on_first_game_in_search_row()
    cart_page.add_game_to_cart()
    cart_page.continue_buying()
    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Manor Lords")
    search_page.click_on_first_game_in_search_row()
    cart_page.add_game_to_cart()
    cart_page.move_to_cart()
    cart_page.clear_cart()

    cart_page.check_empty_cart()
