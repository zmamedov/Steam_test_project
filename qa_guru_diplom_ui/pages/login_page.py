import allure
from selene import browser, have


class LoginPage:
    def click_on_login(self):
        with allure.step('Кликнуть на кнопку "login".'):
            browser.all('.global_action_link').element_by(have.text('login')).click()

    def check_login_page(self):
        with allure.step('Проверить, что отображается страница авторизации.'):
            browser.element('button[type="submit"]').should(have.exact_text('Sign in'))


login_page = LoginPage()
