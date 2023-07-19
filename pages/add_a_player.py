from pages.base_page import BasePage
import time


class AddAPlayer(BasePage):
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    age_field_xpath = "//input[@name='age']"
    main_position_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//*[3]/button[1]/span[1]"
    leg_field_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_xpath = "//li[@data-value='right']"
    left_leg_xpath = "//li[@data-value='left']"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player(self):
        time.sleep(5)
        self.click_on_the_element(self.add_player_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_xpath, main_position)

    def click_on_the_submit(self):
        self.click_on_the_element(self.submit_button_xpath)

    def select_leg(self, leg):
        self.click_on_the_element(self.leg_field_xpath)
        time.sleep(1)
        if leg == "right":
            self.click_on_the_element(self.right_leg_xpath)
        else:
            self.click_on_the_element(self.left_leg_xpath)
