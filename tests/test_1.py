from qa_guru_diplom_ui.pages.main_page import main_page
from qa_guru_diplom_ui.pages.search_page import search_page


def test_switch_tab():
    main_page.open_main_page()
    main_page.switch_navigation_tab(tab_name='СООБЩЕСТВО')

    main_page.check_community_tab_title()


def test_search():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")

    search_page.check_search_result(game_name="Baldur's Gate 3")


def test_change_language():
    main_page.open_main_page()
    main_page.click_on_list_of_lang()
    main_page.choose_lang()
    main_page.check_lang_on_page()


def test_open_login_page():
    main_page.open_main_page()
    main_page.click_on_login()
    main_page.check_login_page()


def test_add_game_to_cart():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")
    search_page.click_on_first_game_in_search_row()
    main_page.add_game_to_cart()
    main_page.open_cart()

    main_page.check_game_in_cart()


def test_remove_game_from_cart():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")
    search_page.click_on_first_game_in_search_row()
    main_page.add_game_to_cart()
    main_page.open_cart()
    main_page.remove_game_from_cart()

    main_page.check_empty_cart()


def test_clear_cart():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")
    search_page.click_on_first_game_in_search_row()
    main_page.add_game_to_cart()
    main_page.open_cart()

    main_page.clear_cart()
    main_page.check_empty_cart()
