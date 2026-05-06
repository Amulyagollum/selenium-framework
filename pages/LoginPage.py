from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver =driver
        self.url = "https://www.saucedemo.com/"

        #locators

        self.username = (By.ID, "user-name")
        self.password =(By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_msg =(By.XPATH, "//h3[@data-test='error']")

    def open(self):
        self.driver.get(self.url)
    
    def login(self,user,pwd):

        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
        self.driver.implicitly_wait(5)

    def get_error(self):
        return self.driver.find_element(*self.error_msg).text


        

