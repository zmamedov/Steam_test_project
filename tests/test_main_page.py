from qa_guru_diplom_ui.pages.main_page import main_page


def test_switch_tab():
    main_page.open_main_page()

    main_page.switch_navigation_tab(tab_name='СООБЩЕСТВО')

    main_page.check_community_tab_title()


def test_change_language():
    main_page.open_main_page()

    main_page.click_on_list_of_lang()
    main_page.choose_lang(lang="french")

    main_page.check_french_lang_on_page()
