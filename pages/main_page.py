from pages.base_page import BasePage
from locators.main_page_loc import MainPageLoc


class MainPage(BasePage):
    def open_regional_settings_page(self):
        regional_settings_page = self.chrome.find_element(*MainPageLoc.button_regional_settings_loc)
        regional_settings_page.click()

    def check_currency(self, currency):
        currency_text = self.chrome.find_element(*MainPageLoc.currency_loc).text
        assert currency_text == f'{currency.upper()}', 'Error: Incorrect currency value!'

    def check_country(self, country:str):
        country_text = self.chrome.find_element(*MainPageLoc.country_loc).text
        assert country_text == f'{country.title()}', 'Error: Incorrect country value'

    def login_with_email_and_password(self, email:str, password:str):
        email_field = self.chrome.find_element(*MainPageLoc.login_email_field_loc)
        email_field.send_keys(f'{email}')

        password_field = self.chrome.find_element(*MainPageLoc.login_password_field_loc)
        password_field.send_keys(f'{password}')

    def check_login_verification(self):
        assert self.is_element_present(MainPageLoc.account_text_loc), 'Error: Element is absent!'

    def login_button_click(self):
        login_button = self.chrome.find_element(*MainPageLoc.button_login_loc)
        login_button.click()

    def open_green_duck_page(self):
        green_duck = self.chrome.find_element(*MainPageLoc.green_duck_loc)
        green_duck.click()

    def logout(self):
        logout_button = self.chrome.find_element(*MainPageLoc.button_logout_loc)
        logout_button.click()

    def open_edit_account_page(self):
        edit_account_page = self.chrome.find_element(*MainPageLoc.button_edit_account_loc)
        edit_account_page.click()
