from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class DriverFactory():

    def __init__(self, browser="chrome"):
        self.browser = browser.lower()
        


    def get_driver(self):

        if self.browser=="chrome":
            options=webdriver.ChromeOptions()
            options.add_argument("--start-maximized")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.implicitly_wait(5)

            return driver
        
        elif self.browser =="firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            driver.implicitly_wait(5)
            return driver
        
        else:
            raise Exception("Browser not supported")
        
