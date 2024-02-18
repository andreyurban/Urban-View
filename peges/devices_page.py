from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DevicesPage(BasePage):

    PAGE_URL = Links.DEVICES

    BUTTON_ADD_DEVICE = ("xpath", "//*[@id='breadcrumbs']/div/div/div/div[1]/a")
    BUTTON_TOGGLE_CONNECTED = ("xpath", "//*[@id='table-filters-row1']/span[1]/label[1]/div/div/label[1]")
    BUTTON_TOGGLE_DISCONNECTED = ("xpath", "//*[@id='table-filters-row1']/span[1]/label[2]/div/div/label[1]")
    BUTTON_TOGGLE_SLEEP = ("xpath", "//*[@id='table-filters-row1']/span[1]/label[3]/div/div/label[1]")
