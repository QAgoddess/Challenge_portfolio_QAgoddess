from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    header_xpath = "//*[@id='__next']/div[1]/header"
    header_text_xpath = "//*[contains(@class, 'jss16')]"
    main_page_xpath = "//div[contains(@class, '443')]"
    players_xpath = "//div[contains(@class, '444')]"
    test_test_xpath = "//div[contains(@class, '445')]"
    matches_xpath = "//span[text()='Matches']"
    reports_xpath = "//span[text()='Reports']"
    polski_xpath = "//span[text()='Polski']"
    sign_out_xpath = "//*[text()='Sign out']"
    add_match_xpath = "//a[contains(@class, '0')]"
    table_xpath = "//table"
    thead_xpath = "//thead"
    tbody_xpath = "//tbody"