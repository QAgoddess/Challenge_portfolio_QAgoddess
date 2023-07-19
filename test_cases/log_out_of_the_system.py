import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

'''Przypadek testowy nr 5, wylogowanie się ze strony głównej'''


class TestAddAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_sign_out()
        time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()