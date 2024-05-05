from selene import browser, have


class LoginPage:
    def click_on_login(self):
        browser.all('[role="navigation"]').element_by(have.text('войти')).click()

    def check_login_page(self):
        browser.element('button[type="submit"]').should(have.exact_text('Войти'))


login_page = LoginPage()
