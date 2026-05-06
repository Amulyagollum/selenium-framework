from selenium.webdriver.common.by import By

class Cartspage:

    def __init__(self, driver):
        self.driver = driver

        self.cart_item = (By.CLASS_NAME, "inventory_item_name")
    
    def get_cart_items(self):
        items = self.driver.find_elements(*self.cart_item)
        return [item.text for item in items]
        
    
    def has_items(self, expected_items):

        actual_items = self.get_cart_items()

        return all(item in actual_items for item in expected_items)
