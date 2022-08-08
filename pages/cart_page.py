from pages.base_page import BasePage
from locators.cart_page_loc import CartPageLoc


class CartPage(BasePage):
    def check_quantity(self):
        quantity_text = (self.chrome.find_element(*CartPageLoc.order_quantity_info_loc)).text
        assert quantity_text == '3', 'Error: Incorrect Quantity!'

    def check_product(self):
        product_text = (self.chrome.find_element(*CartPageLoc.product_text_loc)).text
        assert product_text == 'Green Duck', 'Error: Wrong Product!'

    def click_confirm_order(self):
        confirm_order = (self.chrome.find_element(*CartPageLoc.button_confirm_order_loc))
        confirm_order.click()

    def check_total_price(self):
        quantity_text = (self.chrome.find_element(*CartPageLoc.order_quantity_info_loc)).text
        quantity = int(quantity_text)

        duck_price = (self.chrome.find_element(*CartPageLoc.price_duck_loc)).text
        price = float(''.join(ele for ele in duck_price if ele.isdigit() or ele == '.'))

        total_text = (self.chrome.find_element(*CartPageLoc.total_price_loc)).text
        total = float(''.join(ele for ele in total_text if ele.isdigit() or ele == '.'))
        assert (quantity * price) == total, 'Error: Total price incorrect!'

    def change_quantity_ducks(self):
        quantity = (self.chrome.find_element(*CartPageLoc.quantity_duck_loc))
        quantity.clear()
        quantity.send_keys('3')

    def click_button_update_quantity_ducks(self):
        button_update = (self.chrome.find_element(*CartPageLoc.button_update_loc))
        button_update.click()

    def click_button_remove_ducks(self):
        button_remove = (self.chrome.find_element(*CartPageLoc.button_remove_loc))
        button_remove.click()

    def check_empty_cart(self):
        empty_cart_text = (self.chrome.find_element(*CartPageLoc.empty_cart_text_loc)).text
        assert empty_cart_text == 'There are no items in your cart.'
