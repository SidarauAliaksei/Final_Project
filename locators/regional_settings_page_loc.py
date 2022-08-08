from selenium.webdriver.common.by import By


class RegionalSettingsPageLoc:
    field_select_currency_loc = (By.XPATH, "//*[@name='currency_code']")
    field_select_country_loc = (By.XPATH, "//*[@name='country_code']")

    click_save_loc = (By.XPATH, "//*[text()='Save']")
