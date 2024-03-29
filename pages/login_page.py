import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@name='Input.UserName']")
    PASSWORD_FIELD = ("xpath", "//input[@name='Input.Password']")
    CHECKBOX_REMEMBERME = ("xpath", "//input[@name='Input.RememberMe']")
    BUTTON_LOGIN = ("xpath", "//button[@type='submit']")


    @allure.step("Enter fail login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter fail password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("X on Remember Me")
    def X_on_RememberMe(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_REMEMBERME)).click()

    @allure.step("Click on login button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_LOGIN)).click()
