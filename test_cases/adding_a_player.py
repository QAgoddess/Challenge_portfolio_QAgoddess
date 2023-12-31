import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_a_player import AddAPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

'''Przypadek testowy nr 3, dodawanie gracza (tylko wymagane pola)'''


class TestAddingAPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_adding_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        time.sleep(1)
        dashboard_page.click_on_the_add_player()
        add_a_player_page = AddAPlayer(self.driver)
        time.sleep(2)
        add_a_player_page.type_in_name('Jan')
        time.sleep(2)
        add_a_player_page.type_in_surname('Aktywny')
        time.sleep(2)
        add_a_player_page.type_in_age('19.02.2000')
        time.sleep(2)
        add_a_player_page.type_in_main_position('napastnik')
        time.sleep(2)
        add_a_player_page.click_on_the_submit()
        time.sleep(3)
        add_a_player_page.click_on_main_page()
        time.sleep(3)
        dashboard_page.check_last_created_player()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
