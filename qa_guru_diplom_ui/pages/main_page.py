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

    def click_on_login(self):
        browser.element('[class="global_action_link"]').click()

    def check_community_tab_title(self):
        browser.element('.community_home_title').should(have.exact_text('Активность сообщества'))

    def check_french_lang_on_page(self):
        browser.element('#language_pulldown').should(have.exact_text('langue'))

    def check_login_page(self):
        browser.element('._39uMKt8ePvr2Tw7x1YxJh3').should(have.exact_text('Войти'))

    def add_game_to_cart(self):
        browser.element('.btn_addtocart').click()

    def open_cart(self):
        browser.all('[type="button"]').second.click()

    def check_game_in_cart(self):
        browser.element('.pVXX8Pzc4JbT40TP4RwRG').should(have.exact_text("Baldur's Gate 3"))

    def remove_game_from_cart(self):
        browser.element('._33j4SwfO2YH9eI6qV9BKaL').click()

    def check_empty_cart(self):
        browser.all('._17GFdSD2pc0BquZk5cejg8>div').first.should(have.exact_text("Ваша корзина пуста."))

    def clear_cart(self):
        browser.element('._12zYFuKO2U-1QfeVxlGfwF').click()


main_page = MainPage()
