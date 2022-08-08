from selenium.webdriver.common.by import By


class GreenDuckPageLoc:
    button_add_to_cart_loc = (By.XPATH, "//button[@name='add_cart_product']")

    field_quantity_loc = (By.XPATH, "//input[@name='quantity']")

    cart_loc = (By.XPATH, "//*[@id='cart']")




