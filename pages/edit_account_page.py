from pages.base_page import BasePage
from locators.edit_account_page_loc import EditAccountPageLoc


class EditAccountPage(BasePage):
    def change_first_name(self):
        first_name = self.chrome.find_element(*EditAccountPageLoc.field_first_name_loc)
        first_name.clear()
        first_name.send_keys('Gomer')

    def click_button_save(self):
        button_save = self.chrome.find_element(*EditAccountPageLoc.button_save_loc)
        button_save.click()