import allure
from selene import browser, have


class LoginPage:
    def click_on_login(self):
        with allure.step('Кликнуть на кнопку "войти".'):
            browser.all('.global_action_link').element_by(have.text('войти')).click()

    def check_login_page(self):
        with allure.step('Проверить, что отображается страница авторизации.'):
            browser.element('button[type="submit"]').should(have.exact_text('Войти'))


login_page = LoginPage()
