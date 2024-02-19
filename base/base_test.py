import pytest

from pages.login_page import LoginPage
from pages.control_panel_page import ControlPanelPage
from pages.devices_page import DevicesPage
from config.data import Data


class BaseTest:

    data: Data

    login_page: LoginPage
    control_panel_page: ControlPanelPage
    devices_page: DevicesPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.control_panel_page = ControlPanelPage(driver)
        request.cls.devices_page = DevicesPage(driver)