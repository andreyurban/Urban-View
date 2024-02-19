import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ControlPanelPage(BasePage):
    PAGE_URL = Links.CONTROL_PANEL

    SWITCHER_MONITORED = ("xpath", "//*[@id='servicelevel-switch']/label[1]/input")
    SWITCHER_BY_CALL = ("xpath", "//*[@id='servicelevel-switch']/label[2]/input")
    CHECKBOX_INTERACTIVE_PIS = ("xpath", "//*[@id='chart-option-XPIS']")
    CHECKBOX_CITY_INFO_POINT = ("xpath", "//*[@id='chart-option-CityInfo']")
    CHECKBOX_MINI_INTERACTIVE_PIS = ("xpath", "//*[@id='chart-option-MiniXPIS']")
    CHECKBOX_SOLAR_PIS = ("xpath", "//*[@id='chart-option-SolarPIS']")
    CHECKBOX_LED_PIS = ("xpath", "//*[@id='chart-option-LedPIS']")


    def click_By_Call(self):
        self.wait.until(EC.element_to_be_clickable(self.SWITCHER_BY_CALL)).click()


    def click_Monitored(self):
        self.wait.until(EC.element_to_be_clickable(self.SWITCHER_MONITORED)).click()


    def click_Interactive_PIS(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_INTERACTIVE_PIS)).click()


    def click_City_Info_Point(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_CITY_INFO_POINT)).click()


    def click_Mini_Interactive_PIS(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_MINI_INTERACTIVE_PIS)).click()


    def click_Solar_PIS(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_SOLAR_PIS)).click()


    def click_Led_Pis(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_LED_PIS)).click()


