 from pages.base_page import BasePage


 class LoginPage(BasePage):
     login_field_xpath = "//*[@id='login']"
     password_field_xpath = "//*[@id='password']"
     sign_in_button_xpath = "//*[text()='Sign in']"
     remind_password_hyperlink_xpath = "//*[text()='Remind password']"
     english_xpath = "//*[text()='English']"


     def type_in_email(self, email):
         self.field_send_keys(self.login_field_xpath, email)
