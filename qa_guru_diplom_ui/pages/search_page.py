from selene import browser, have


class SearchPage:
    def click_on_search(self):
        browser.element('#store_nav_search_term').click()

    def find_game_in_search(self, game_name):
        browser.element('#store_nav_search_term').type(game_name).press_enter()

    def click_on_first_game_in_search_row(self):
        browser.all('.search_result_row').first.click()

    def check_search_result(self, game_name):
        browser.element('.title').should(have.exact_text(game_name))


search_page = SearchPage()
