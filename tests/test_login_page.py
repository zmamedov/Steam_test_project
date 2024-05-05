from qa_guru_diplom_ui.pages.main_page import main_page
from qa_guru_diplom_ui.pages.login_page import login_page


def test_open_login_page():
    main_page.open_main_page()

    login_page.click_on_login()

    login_page.check_login_page()
