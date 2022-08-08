import time
from pages.base_page import BasePage
from locators.green_duck_page_loc import GreenDuckPageLoc


class GreenDuckPage(BasePage):
    def change_quantity_for_add_to_basket(self):
        change_quantity = (self.chrome.find_element(*GreenDuckPageLoc.field_quantity_loc))
        change_quantity.clear()
        change_quantity.send_keys('3')

    def add_to_cart(self):
        button_add_to_cart = (self.chrome.find_element(*GreenDuckPageLoc.button_add_to_cart_loc))
        button_add_to_cart.click()

    def go_to_cart(self):
        time.sleep(1)
        cart = (self.chrome.find_element(*GreenDuckPageLoc.cart_loc))
        cart.click()
