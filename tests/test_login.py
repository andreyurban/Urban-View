import allure
from base.base_test import BaseTest
import pytest
import time


@allure.feature("Testing login Functional")
class TestLoginFeature(BaseTest):

    @allure.title("Test login")
    @allure.severity("Critical")
    @pytest.mark.positive  # negative or positive
    def test_login(self):
        self.login_page.open()
        self.login_page.is_opend()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.X_on_RememberMe()
        self.login_page.click_submit_button()
        time.sleep(1)
        self.login_page.make_screenshot("Success")



    @allure.title("Test login with Wrong Username and Password")
    @allure.severity("Critical")
    @pytest.mark.negative   # negative or positive
    def test_fail_login(self):
        self.login_page.open()
        self.login_page.is_opend()
        self.login_page.enter_login(self.data.WRONG_LOGIN)
        self.login_page.enter_password(self.data.WRONG_PASSWORD)
        self.login_page.X_on_RememberMe()
        self.login_page.click_submit_button()
        time.sleep(1)
        self.login_page.make_screenshot("Success")
