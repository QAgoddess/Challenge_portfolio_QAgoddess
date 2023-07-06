from pages.base_page import BasePage


class Dashboard(BasePage):
    header_xpath = "//*[@id='__next']/div[1]/header"
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
