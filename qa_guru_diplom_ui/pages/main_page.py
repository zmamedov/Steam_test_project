from selene import browser, have


class MainPage:
    def open_main_page(self):
        browser.open('/')

    def switch_navigation_tab(self, tab_name):
        browser.all('.content .supernav').element_by(have.text(tab_name)).click()

    def click_on_list_of_lang(self):
        browser.element('#language_pulldown').click()

    def choose_lang(self, lang):
        browser.element(f'[onclick*="{lang}"]').click()

    def check_community_tab_title(self):
        browser.element('.community_home_title').should(have.exact_text('Активность сообщества'))

    def check_french_lang_on_page(self):
        browser.element('#language_pulldown').should(have.exact_text('langue'))


main_page = MainPage()
