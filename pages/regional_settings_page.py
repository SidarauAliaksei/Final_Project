from pages.base_page import BasePage
from locators.regional_settings_page_loc import RegionalSettingsPageLoc
from selenium.webdriver.support.select import Select


class RegionalSettingsPage(BasePage):
    def change_currency_value(self):
        select_currency_euro = Select(self.chrome.find_element(*RegionalSettingsPageLoc.field_select_currency_loc))
        select_currency_euro.select_by_visible_text('Euros')

    def change_country_value(self):
        select_country_belarus = Select(self.chrome.find_element(*RegionalSettingsPageLoc.field_select_country_loc))
        select_country_belarus.select_by_visible_text('Belarus')

    def click_button_save(self):
        click_button_save = (self.chrome.find_element(*RegionalSettingsPageLoc.click_save_loc))
        click_button_save.click()
