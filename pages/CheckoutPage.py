from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):

        self.driver = driver

        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_post_code = (By.ID, "postal-code")

        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")

        self.success_msg = (By.CLASS_NAME, "complete-header")

    def fill_details(self, first, last, zip_code):

        self.driver.find_element(*self.first_name).clear()
        self.driver.find_element(*self.first_name).send_keys(first)

        self.driver.find_element(*self.last_name).clear()
        self.driver.find_element(*self.last_name).send_keys(last)

        self.driver.find_element(*self.zip_post_code).clear()
        self.driver.find_element(*self.zip_post_code).send_keys(zip_code)

        return self

    def continue_checkout(self):

        self.driver.find_element(*self.continue_btn).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.finish_btn)
        )

        return self

    def finish_checkout(self):

        self.driver.find_element(*self.finish_btn).click()

        return self

    def get_success_message(self):

        return self.driver.find_element(*self.success_msg).text