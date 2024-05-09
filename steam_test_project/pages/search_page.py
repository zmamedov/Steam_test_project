import allure
from selene import browser, have


class SearchPage:
    def click_on_search(self):
        with allure.step('Кликнуть на поле поиска.'):
            browser.element('#store_nav_search_term').click()

    def find_game_in_search(self, game_name):
        with allure.step(f'Ввести в поле поиска "{game_name}".'):
            browser.element('#store_nav_search_term').type(game_name).press_enter()

    def click_on_first_game_in_search_row(self):
        with allure.step('Кликнуть на первый результат поиска.'):
            browser.all('.search_result_row').first.click()

    def check_search_result(self, game_name):
        with allure.step(f'Проверить, что была найдена игра "{game_name}".'):
            browser.element('.title').should(have.exact_text(game_name))


search_page = SearchPage()
