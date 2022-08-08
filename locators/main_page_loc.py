from selenium.webdriver.common.by import By


class MainPageLoc:
    button_login_loc = (By.XPATH, "//button[@name ='login']")
    button_edit_account_loc = (By.XPATH, "//a[text()='Edit Account']")
    button_regional_settings_loc = (By.XPATH, "//*[text()='Regional Settings']")
    button_logout_loc = (By.XPATH, "//*[text()='Logout']")

    login_email_field_loc = (By.XPATH, "//*[@type ='text']")
    login_password_field_loc = (By.XPATH, "//*[@type ='password']")

    account_text_loc = (By.XPATH, "//h3[text()='Account']")

    currency_loc = (By.CLASS_NAME, "currency")
    country_loc = (By.CLASS_NAME, "country")
    green_duck_loc = (By.XPATH, "//img[@alt='Green Duck']")


