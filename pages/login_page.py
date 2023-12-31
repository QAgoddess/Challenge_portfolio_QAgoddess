import time
from pages.base_page import BasePage


class LoginPage(BasePage):
    header_xpath = "//*/h5"
    expected_header = "Scouts Panel"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    zaloguj_xpath = "//*[text()='Zaloguj']"
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    english_xpath = "//*[text()='English']"
    login_url = 'https://dareit.futbolkolektyw.pl/login'
    expected_title = "Scouts panel - sign in"
    language_field_xpath = "//div[2]/div/div"
    english_xpath = "//div[3]/ul/li[2]"
    polski_xpath = "//div[3]/ul/li[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_header_text(self):
        self.assert_element_text(self.driver, self.header_xpath, self.expected_header)

    def select_language(self, language):
        self.click_on_the_element(self.language_field_xpath)
        time.sleep(1)
        if language == "english":
            self.click_on_the_element(self.english_xpath)
        else:
            self.click_on_the_element(self.polski_xpath)
