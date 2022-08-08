import allure
from db_queries import *
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.green_duck_page import GreenDuckPage
from pages.edit_account_page import EditAccountPage
from pages.regional_settings_page import RegionalSettingsPage


link = 'http://localhost/litecart/en/'


@allure.feature('Testing the LiteCartStore')
class TestLiteCartStore:
    @allure.story('Guest can change of currency and country')
    def test_guest_can_change_of_currency_and_country(self, browser):
        with allure.step('Opening main page'):
            main_page = MainPage(browser, link)
            main_page.open()
        with allure.step('Opening regional settings page'):
            main_page.open_regional_settings_page()
            regional_settings_page = RegionalSettingsPage(browser, url=browser.current_url)
        with allure.step('Changing currency'):
            regional_settings_page.change_currency_value()
        with allure.step('Changing country'):
            regional_settings_page.change_country_value()
        with allure.step('Save changes'):
            regional_settings_page.click_button_save()
        with allure.step('Checking currency and country changes on the home page'):
            main_page = MainPage(browser, url=browser.current_url)
            main_page.check_currency_and_country()

    @allure.story('User can login and added ducks in cart')
    def test_user_can_login_and_added_ducks_in_cart(self, browser):
        with allure.step('Opening main page'):
            main_page = MainPage(browser, link)
            main_page.open()
        with allure.step('Entering email and password for login'):
            main_page.login_with_alex_user()
        with allure.step('Pressing the login button'):
            main_page.login_button_click()
        with allure.step('Checking login verification'):
            main_page.check_login_verification()
        with allure.step('Opening the page with green duck'):
            main_page.open_green_duck_page()
            green_duck_page = GreenDuckPage(browser, url=browser.current_url)
        with allure.step('Changing quantity ducks'):
            green_duck_page.change_quantity_for_add_to_basket()
        with allure.step('Adding duck to cart'):
            green_duck_page.add_to_cart()
        with allure.step('Opening cart page'):
            green_duck_page.go_to_cart()
            cart_page = CartPage(browser, url=browser.current_url)
        with allure.step('Checking select quantity'):
            cart_page.check_quantity()
        with allure.step('Checking select ducks'):
            cart_page.check_product()
        with allure.step('Checking total price'):
            cart_page.check_total_price()
        with allure.step('Confirm order'):
            cart_page.click_confirm_order()
        with allure.step('Checking order in db'):
            check_order_in_db()

    @allure.story('User can login and change name')
    def test_user_can_login_and_change_name(self, browser):
        with allure.step('Opening main page'):
            main_page = MainPage(browser, link)
            main_page.open()
        with allure.step('Entering email and password for login'):
            main_page.login_with_bart_user()
        with allure.step('Pressing the login button'):
            main_page.login_button_click()
        with allure.step('Checking login verification'):
            main_page.check_login_verification()
        with allure.step('Opening edit account page'):
            main_page.open_edit_account_page()
            edit_account_page = EditAccountPage(browser, url=browser.current_url)
        with allure.step('Changing first name'):
            edit_account_page.change_first_name()
        with allure.step('Save changes'):
            edit_account_page.click_button_save()
        with allure.step('Checking changes first name'):
            check_changed_first_name()

    @allure.story('User can login and check remove duck after added in cart')
    def test_user_can_login_and_check_remove_duck_after_added_in_cart(self, browser):
        with allure.step('Opening main page'):
            main_page = MainPage(browser, link)
            main_page.open()
        with allure.step('Entering email and password for login'):
            main_page.login_with_bart_user()
        with allure.step('Pressing the login button'):
            main_page.login_button_click()
        with allure.step('Checking login verification'):
            main_page.check_login_verification()
        with allure.step('Opening the page with green duck'):
            main_page.open_green_duck_page()
            green_duck_page = GreenDuckPage(browser, url=browser.current_url)
        with allure.step('Adding duck to cart'):
            green_duck_page.add_to_cart()
        with allure.step('Opening cart page'):
            green_duck_page.go_to_cart()
            cart_page = CartPage(browser, url=browser.current_url)
        with allure.step('Changing quantity ducks'):
            cart_page.change_quantity_ducks()
        with allure.step('Update changes'):
            cart_page.click_button_update_quantity_ducks()
        with allure.step('Checking total price'):
            cart_page.check_total_price()
        with allure.step('Removing ducks from cart'):
            cart_page.click_button_remove_ducks()
        with allure.step('Checking empty cart'):
            cart_page.check_empty_cart()


