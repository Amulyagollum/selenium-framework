from selenium.webdriver.common.by import By
from pages.CheckoutPage import CheckoutPage

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

    def remove_item(self, item_name):
        remove_item_locator = (By.XPATH,f"//button[@data-test='remove-{item_name}']")
        self.driver.find_element(*remove_item_locator).click()
        return self
    
    def continue_shopping(self):
        from pages.InventoryPage import InventoryPage
        continue_shopping_locator=(By.ID, "continue-shopping")
        self.driver.find_element(*continue_shopping_locator).click()
        return InventoryPage(self.driver)
    
    def checkout(self):
        checkout_locator=(By.ID, "checkout")
        self.driver.find_element(*checkout_locator).click()

        return CheckoutPage(self.driver)

