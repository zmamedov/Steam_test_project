from selene import browser, have


def test_switch_tab():
    browser.open('/')
    browser.element('.responsive_page_content [data-tooltip-content=".submenu_Community"]').click()

    browser.element('.community_home_title').should(have.exact_text('Активность сообщества'))


def test_search():
    browser.open('/')

    browser.element('#store_nav_search_term').click()
    browser.element('#store_nav_search_term').type("Baldur's Gate 3").press_enter()
    browser.element('.title').should(have.exact_text("Baldur's Gate 3"))


def test_change_language():
    browser.open('/')
    browser.element('#language_pulldown').click()
    browser.element('[onclick*="french"]').click()
    browser.element('#language_pulldown').should(have.exact_text('langue'))


def test_open_login_page():
    browser.open('/')
    browser.element('[class="global_action_link"]').click()
    browser.element('._39uMKt8ePvr2Tw7x1YxJh3').should(have.exact_text('Войти'))



def test_add_game_to_cart():
    browser.open('/')
    browser.element('#store_nav_search_term').click()
    browser.element('#store_nav_search_term').type("Baldur's Gate 3").press_enter()
    browser.all('.search_result_row').first.click()
    browser.element('.btn_addtocart').click()
    browser.all('[type="button"]').second.click()
    browser.element('.pVXX8Pzc4JbT40TP4RwRG').should(have.exact_text("Baldur's Gate 3"))




def test_remove_game_from_cart():
    browser.open('/')
    browser.element('#store_nav_search_term').click()
    browser.element('#store_nav_search_term').type("Baldur's Gate 3").press_enter()
    browser.all('.search_result_row').first.click()
    browser.element('.btn_addtocart').click()
    browser.all('[type="button"]').second.click()
    browser.element('._33j4SwfO2YH9eI6qV9BKaL').click()
    browser.all('._17GFdSD2pc0BquZk5cejg8>div').first.should(have.exact_text("Ваша корзина пуста."))

def test_clear_cart():
    browser.open('/')
    browser.element('#store_nav_search_term').click()
    browser.element('#store_nav_search_term').type("Baldur's Gate 3").press_enter()
    browser.all('.search_result_row').first.click()
    browser.element('.btn_addtocart').click()
    browser.all('[type="button"]').second.click()
    browser.element('._12zYFuKO2U-1QfeVxlGfwF').click()
    browser.all('._17GFdSD2pc0BquZk5cejg8>div').first.should(have.exact_text("Ваша корзина пуста."))
