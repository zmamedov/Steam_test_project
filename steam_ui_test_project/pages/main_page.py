import allure
from selene import browser, have


class MainPage:
    def open_main_page(self):
        with allure.step('Открыть главную страницу "Steam".'):
            browser.open('/')

    def switch_navigation_tab(self, tab_name):
        with allure.step(f'Переключиться на вкладку "{tab_name}".'):
            browser.all('.content .supernav').element_by(have.text(tab_name)).click()

    def click_on_list_of_lang(self):
        with allure.step('Кликнуть на список доступных языков.'):
            browser.element('#language_pulldown').click()

    def choose_lang(self, lang):
        with allure.step('Выбрать французский язык.'):
            browser.element(f'[onclick*="{lang}"]').click()

    def check_community_tab_title(self):
        with allure.step('Проверить заголовок вкладки "Community Activity".'):
            browser.element('.community_home_title').should(have.exact_text('Community Activity'))

    def check_french_lang_on_page(self):
        with allure.step('Проверить, что на странице установлен французский язык.'):
            browser.element('#language_pulldown').should(have.exact_text('langue'))


main_page = MainPage()
