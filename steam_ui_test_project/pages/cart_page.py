import allure
from selene import browser, have


class CartPage:
    def add_game_to_cart(self):
        with allure.step('Добавить игру в корзину.'):
            browser.element('.btn_addtocart').click()

    def move_to_cart(self):
        with allure.step('Перейти в корзину.'):
            browser.all('[type="button"]').element_by(have.text('View My Cart')).click()

    def continue_buying(self):
        with allure.step('Продолжить покупки.'):
            browser.all('[type="button"]').element_by(have.text('Continue Shopping')).click()

    def remove_game_from_cart(self):
        with allure.step('Удалить игру из корзины.'):
            browser.element('._33j4SwfO2YH9eI6qV9BKaL').click()

    def clear_cart(self):
        with allure.step('Очистить корзину.'):
            browser.element('._12zYFuKO2U-1QfeVxlGfwF').click()

    def check_game_in_cart(self, game_name):
        with allure.step('Проверить игру в корзине.'):
            browser.element('.pVXX8Pzc4JbT40TP4RwRG').should(have.exact_text(game_name))

    def check_empty_cart(self):
        with allure.step('Проверить, что корзина пустая.'):
            browser.all('._17GFdSD2pc0BquZk5cejg8>div').first.should(have.exact_text("Your cart is empty."))


cart_page = CartPage()
