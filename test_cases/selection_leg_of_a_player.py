import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddAPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSelectLeg(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_select_leg(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player()
        add_a_player_page = AddAPlayer(self.driver)
        time.sleep(2)
        add_a_player_page.select_leg("right")
        time.sleep(3)
        add_a_player_page.select_leg("left")
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
