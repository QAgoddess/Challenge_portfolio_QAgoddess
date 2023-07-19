import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    header_text_xpath = "//*[contains(@class, 'jss16')]"
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//*[text()='Players']"
    polski_xpath = "//*[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    logo_xpath = "//*[contains(@title, 'L')]"
    name_logo_xpath = "//h2[text()='Scouts Panel']"
    subtitle_scouts_panel_xpath = "//p[contains(@class, 'Mui')]"
    dev_team_contact_xpath = "//a[contains(@tabindex, '0')]"
    add_player_xpath = "//*[text()='Add player']"
    activity_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h2"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.sign_out_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player(self):
        time.sleep(5)
        self.click_on_the_element(self.add_player_xpath)

    def click_on_the_sign_out(self):
        time.sleep(5)
        self.click_on_the_element(self.sign_out_xpath)
