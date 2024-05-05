from qa_guru_diplom_ui.pages.main_page import main_page
from qa_guru_diplom_ui.pages.search_page import search_page


def test_search():
    main_page.open_main_page()

    search_page.click_on_search()
    search_page.find_game_in_search(game_name="Baldur's Gate 3")

    search_page.check_search_result(game_name="Baldur's Gate 3")
