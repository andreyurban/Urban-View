import time
from peges.base_page import BasePage
from conftest import driver


def test(driver):
    page = BasePage(driver, 'https://xpis.urban-digital.co.il:7011/')
    page.open()
    time.sleep(3)
