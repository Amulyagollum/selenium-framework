from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self,driver):
        self.driver = driver

    def is_loaded(self):
        self.driver.find_element(By.ID, "inventory_container").is_displayed()
    
    def add_item_to_cart(self, item_name):
        locator = (By.XPATH, f"//button[@data-test='add-to-cart-{item_name}']")
        self.driver.find_element(*locator).click()
        return self
    
    def add_mutiple_items_to_cart(self, item_list):
         for item in item_list:
            locator = (By.XPATH, f"//button[@data-test='add-to-cart-{item}']")
            self.driver.find_element(*locator).click()
    
            return self   
    
    def go_to_cart(self):
        from pages.CartsPage import Cartspage
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        return Cartspage(self.driver)

    def continue_shoppinf(self):
        return self
  