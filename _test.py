from Pages import clicks
import time
import allure


def test_holders(browser, self=None):
    main_page = clicks(browser)
    main_page.go_to_site()
    main_page.click_logo()
    main_page.holders()
    main_page.click_top_dfx_price()

def test_menu_guarantees(browser):
    main_page = clicks(browser)
    main_page.go_to_site()
    main_page.guarantees()

def test_menu_clicks(browser):
    main_page = clicks(browser)
    main_page.go_to_site()
    main_page.menu_clicks()

def test_buy_DFX(browser):
    main_page = clicks(browser)
    main_page.go_to_site()
    main_page.buy()

def test_read_article_and_proofs(browser):
    main_page = clicks(browser)
    main_page.go_to_site()
    main_page.read_article_and_proofs()

def test_footer(browser):
    main_page = clicks(browser)
    main_page.go_to_site()
    main_page.footer()

def test_test_FAQ(browser):
    main_page = clicks(browser)
    main_page.go_to_site()
    main_page.FAQ1()
    main_page.FAQ2()
    main_page.FAQ3()
    main_page.FAQ4()
    main_page.FAQ5()


test_holders()
test_menu_guarantees()
test_menu_clicks()
test_buy_DFX()
test_read_article_and_proofs()
test_footer()
test_test_FAQ()







