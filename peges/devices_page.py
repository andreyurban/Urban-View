from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DevicesPage(BasePage):

    PAGE_URL = Links.DEVICES

    BUTTON_ADD_DEVICE = ("xpath", "//a[@href='/Devices/Create']")
    FILTER_CONNECTED = ("xpath", "//input[@data-status='1']")
    FILTER_DISCONNECTED = ("xpath", "//input[@data-status='2']")
    FILTER_SLEEP = ("xpath", "//input[@data-status='6']")
    FILTER_NEVER_CONNECTED = ("xpath", "//input[@data-status='3']")
    FILTER_IN_TREATMENT = ("xpath", "//input[@data-status='4']")
    FILTER_TESTS = ("xpath", "//input[@data-status='5']")

    def click_add_device(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_DEVICE)).click()

    def filter_connected(self):
        self.wait.until(EC.e(self.FILTER_CONNECTED)).click()

    def filter_disconnected(self):
        self.wait.until(EC.element_to_be_clickable(self.FILTER_DISCONNECTED)).click()

    def filter_sleep(self):
        self.wait.until(EC.element_to_be_clickable(self.FILTER_SLEEP)).click()

    def filter_never_connected(self):
        self.wait.until(EC.element_to_be_clickable(self.FILTER_NEVER_CONNECTED)).click()

    def filter_in_treatment(self):
        self.wait.until(EC.element_to_be_clickable(self.FILTER_IN_TREATMENT)).click()

    def filter_tests(self):
        self.wait.until(EC.element_to_be_clickable(self.FILTER_TESTS)).click()
