from selenium.webdriver.common.by import By


class CartPageLoc:
    button_update_loc = (By.XPATH, "//button[@name='update_cart_item']")
    button_remove_loc = (By.XPATH, "//button[@name='remove_cart_item']")
    button_confirm_order_loc = (By.XPATH, "//button[@name='confirm_order']")

    empty_cart_text_loc = (By.XPATH, "//*[text()='There are no items in your cart.']")
    product_text_loc = (By.XPATH, "//td[@class='item']")

    quantity_duck_loc = (By.XPATH, "//input[@ name = 'quantity']")
    order_quantity_info_loc = (By.XPATH, "//td[@style='text-align: center;']")
    total_price_loc = (By.XPATH, "//td[@class='sum']")
    price_duck_loc = (By.CSS_SELECTOR, "p:nth-child(2)")