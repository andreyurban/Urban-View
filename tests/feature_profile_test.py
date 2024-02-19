import allure
from base.base_test import BaseTest
import pytest

@allure.feature("Testing login Functional")
class TestLoginFeature(BaseTest):

    @allure.title("Test fail login")
    @allure.severity("Critical")
    @pytest.mark.usefixtures("driver")
    def test_fail_login(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.X_on_RememberMe()
        self.login_page.click_submit_button()
        self.login_page.make_screenshot("Success")
