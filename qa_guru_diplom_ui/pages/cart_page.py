from selene import browser, have


class CartPage:
    def add_game_to_cart(self):
        browser.element('#btn_add_to_cart_478012').click()

    def move_to_cart(self):
        browser.all('[type="button"]').element_by(have.text('Открыть корзину'))

    def continue_buying(self):
        browser.all('[type="button"]').element_by(have.text('Продолжить покупки'))

    def remove_game_from_cart(self):
        browser.element('._33j4SwfO2YH9eI6qV9BKaL').click()

    def clear_cart(self):
        browser.element('._12zYFuKO2U-1QfeVxlGfwF').click()

    def check_game_in_cart(self, game_name):
        browser.element('.pVXX8Pzc4JbT40TP4RwRG').should(have.exact_text(game_name))

    def check_empty_cart(self):
        browser.all('._17GFdSD2pc0BquZk5cejg8>div').first.should(have.exact_text("Ваша корзина пуста."))


cart_page = CartPage()
