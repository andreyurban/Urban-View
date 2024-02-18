from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)


    def open(self):
        self.driver.get(self.PAGE_URL)


    def is_opend(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))
